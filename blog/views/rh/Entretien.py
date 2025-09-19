from django.shortcuts import render, redirect, get_object_or_404
from blog.models.rh.rh import *
from blog.models.rh.Annonce import *
from blog.models.rh.Candidat import *
from django.db.models import Sum
from django.db.models import Exists, OuterRef

def planning(request):
    # Récupérer les plannings restants : pas encore notés ET dont l’annonce n’est pas fermée
    plannings = (
        PlanningEntretien.objects
        .select_related("id_candidat", "id_annonce")
        .annotate(
            has_score=Exists(
                ScoreEntretien.objects.filter(
                    id_candidat=OuterRef("id_candidat"),
                    id_annonce=OuterRef("id_annonce")
                )
            )
        )
        .filter(has_score=False)  # uniquement sans note
        .exclude(id_annonce__annoncestatus__status=True)  # exclure annonces fermées
        .order_by("date_entretien")
    )

    context = {
        "plannings": plannings
    }
    return render(request, "rh/planning_list.html", context)

def evaluation(request, planning_id):

    planning = get_object_or_404(PlanningEntretien, id=planning_id)
    candidat = planning.id_candidat
    annonce = planning.id_annonce

    try:
        cv = CV.objects.get(candidat=candidat, annoncecv__annonce=annonce)
    except CV.DoesNotExist:
        cv = None


    return render(request, "rh/evaluation.html", {
        "planning": planning,
        "candidat": candidat,
        "cv": cv
    })

def evaluation_score(request):
    candidat_id = request.POST.get("candidat_id")
    planning_id = request.POST.get("planning_id")

    planning = get_object_or_404(PlanningEntretien, id=planning_id)
    candidat = planning.id_candidat

    try:
        cv = CV.objects.get(candidat=candidat, annoncecv__annonce=planning.id_annonce)
    except CV.DoesNotExist:
        cv = None

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

    # Création du score d’entretien
    ScoreEntretien.objects.create(
        note=point,
        id_candidat=candidat,
        id_annonce=planning.id_annonce
    )

    # Calcul du total QCM
    total_score_qcm = ScoreQuestion.objects.filter(
        id_candidat=candidat,
        id_annonce=planning.id_annonce
    ).aggregate(total=Sum('note'))['total'] or 0

    # Note finale
    note_total = (point + (total_score_qcm * 2)) / 2

    ScoreTotal.objects.create(
        id_candidat=candidat,
        id_annonce=planning.id_annonce,
        note=note_total
    )

    # Met à jour le statut du CV si réussite
    if note_total >= 10 and cv:
        cv.statut = StatutCV.objects.get(description='entretien reussi')
        cv.save()

    # Récupérer les plannings restants : pas encore notés ET dont l’annonce n’est pas fermée
    plannings = (
        PlanningEntretien.objects
        .select_related("id_candidat", "id_annonce")
        .annotate(
            has_score=Exists(
                ScoreEntretien.objects.filter(
                    id_candidat=OuterRef("id_candidat"),
                    id_annonce=OuterRef("id_annonce")
                )
            )
        )
        .filter(has_score=False)  # uniquement sans note
        .exclude(id_annonce__annoncestatus__status=True)  # exclure annonces fermées
        .order_by("date_entretien")
    )

    context = {
        "plannings": plannings
    }
    return render(request, "rh/planning_list.html", context)
