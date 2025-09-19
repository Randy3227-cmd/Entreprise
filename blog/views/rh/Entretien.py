from django.shortcuts import render, redirect, get_object_or_404
from blog.models.rh.rh import *
from blog.models.rh.Annonce import *
from blog.models.rh.Candidat import *
from django.db.models import Sum

def planning(request):
    plannings = PlanningEntretien.objects.select_related("id_candidat").all().order_by("date_entretien")

    context = {
        "plannings": plannings
    }
    return render(request, "rh/planning_list.html", context)

def evaluation(request, planning_id):
    # Récupération du planning et du candidat
    planning = get_object_or_404(PlanningEntretien, id=planning_id)
    candidat = get_object_or_404(Candidat, id=planning.id_candidat.id)
    annonce = planning.id_annonce

    # Récupération du CV du candidat pour cette annonce
    try:
        annonce_cv = AnnonceCV.objects.get(annonce=annonce, cv__candidat=candidat)
        cv = annonce_cv.cv
    except AnnonceCV.DoesNotExist:
        cv = None  # Aucun CV trouvé pour ce candidat et cette annonce

    return render(request, "rh/evaluation.html", {
        "planning": planning,
        "candidat": candidat,
        "cv": cv
    })

def evaluation_score (request):
    candidat_id = request.POST.get("candidat_id")
    planning_id = request.POST.get("planning_id")

    planning = get_object_or_404(PlanningEntretien, id=planning_id)
    candidat = get_object_or_404(Candidat, id=candidat_id)

    score = request.POST.get("score")
    point = 0

    if score is not None:
        score = int(score)
        if score == -1: 
            point = 6
        elif score == 0:
            point = 10
        elif score == 1:
            point = 12
        elif score == 2:
            point = 16
        
    ScoreEntretien.objects.create(
        note=point,
        id_candidat=candidat,
        id_annonce=planning.id_annonce
    )

    total_score_qcm = ScoreQuestion.objects.filter(
        id_candidat=candidat,
        id_annonce=planning.id_annonce
    ).aggregate(total=Sum('note'))['total'] or 0

    note_total = (point + (total_score_qcm * 2)) / 2

    ScoreTotal.objects.create(
        id_candidat=candidat,
        id_annonce=planning.id_annonce,
        note=note_total
    )

    plannings = PlanningEntretien.objects.select_related("id_candidat").all().order_by("date_entretien")

    context = {
        "plannings": plannings
    }
    return render(request, "rh/planning_list.html", context)