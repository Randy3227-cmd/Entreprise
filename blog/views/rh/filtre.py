from django.shortcuts import render
from blog.models.rh import *
from django.utils import timezone
from django.db.models import Q
from datetime import date
from django.http import HttpResponse

def annonce_list(request):
    annonces = Annonce.objects.all()

    # récupérer paramètres
    poste_id = request.GET.get("poste")
    salaire_min = request.GET.get("salaire_min")
    salaire_max = request.GET.get("salaire_max")
    lieu = request.GET.get("lieu")
    horaire = request.GET.get("horaire")
    date_limite = request.GET.get("date_limite")

    # appliquer filtres indépendants
    if poste_id:
        annonces = annonces.filter(poste_id=poste_id)
    if salaire_min:
        annonces = annonces.filter(salaire__gte=salaire_min)
    if salaire_max:
        annonces = annonces.filter(salaire__lte=salaire_max)
    if lieu:
        annonces = annonces.filter(lieu_de_poste__icontains=lieu)
    if horaire:
        annonces = annonces.filter(horaire_de_travail=horaire)
    if date_limite:
        annonces = annonces.filter(date_limite_postule__gte=date_limite)
    else:
        annonces = annonces.filter(date_limite_postule__gte=timezone.now())

    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        return render(request, "rh/annonce_results.html", {"annonces": annonces})

    return render(request, "rh/annonce_list.html", {"annonces": annonces, "postes": Poste.objects.all()})


def candidat_list(request):
    cvs = CV.objects.select_related("candidat", "statut").all()

    # Filtres classiques (formation, âge, adresse, etc.)
    formation = request.GET.get("formation")
    age_min = request.GET.get("age_min")
    age_max = request.GET.get("age_max")
    adresse = request.GET.get("adresse")
    annonce_id = request.GET.get("annonce")
    date_creation = request.GET.get("date_creation")
    experience = request.GET.get("experience")
    nom = request.GET.get("nom")
    prenom = request.GET.get("prenom")
    statut = request.GET.get("statut")

    today = date.today()
    if formation:
        cvs = cvs.filter(formations__formation_id=formation)
    if age_min:
        max_birthdate = date(today.year - int(age_min), today.month, today.day)
        cvs = cvs.filter(candidat__date_naissance__lte=max_birthdate)
    if age_max:
        min_birthdate = date(today.year - int(age_max), today.month, today.day)
        cvs = cvs.filter(candidat__date_naissance__gte=min_birthdate)
    if adresse:
        cvs = cvs.filter(candidat__adresse__icontains=adresse)
    if annonce_id:
        cvs = cvs.filter(annoncecv__annonce_id=annonce_id)
    if date_creation:
        cvs = cvs.filter(date_creation__gte=date_creation)
    if experience:
        cvs = cvs.filter(formations__etablissement__icontains=experience)
    if nom:
        cvs = cvs.filter(candidat__nom__icontains=nom)
    if prenom:
        cvs = cvs.filter(candidat__prenom__icontains=prenom)
    if statut:
        cvs = cvs.filter(statut_id=statut)

    # Retourne seulement le fragment si AJAX
    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        return render(request, "rh/candidat_results.html", {"cvs": cvs})

    return render(request, "rh/candidat_list.html", {
        "cvs": cvs,
        "formations": Formation.objects.all(),
        "annonces": Annonce.objects.all(),
        "statuts": StatutCV.objects.all(),
    })
