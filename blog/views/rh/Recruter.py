from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from blog.models.rh.Annonce import *
from blog.models.rh.Candidat import * 
from blog.models.rh.Employe import *
from blog.models.rh.rh import AnnonceStatus
from django.urls import reverse
from django.http import JsonResponse

def recruter(request, annonce_id):
    annonce = get_object_or_404(Annonce, id=annonce_id)

    if request.method == "POST":
        candidat_id = request.POST.get("candidat_id")
        salaire = request.POST.get("salaire")
        poste_id = annonce.poste.id

        candidat = get_object_or_404(Candidat, id=candidat_id)
        cv = get_object_or_404(CV, candidat=candidat)

        # Créer l'employé
        employe = Employe.objects.create(
            salaire=salaire,
            candidat=candidat,
            poste_id=poste_id
        )

        if cv.statut.description != 'Recrute':
            cv.statut = StatutCV.objects.get(description='Recrute')
            cv.save()

        # Mettre à jour le statut de l'annonce
        annonceStatus = AnnonceStatus.objects.get(annonce=annonce)
        annonceStatus.status = True
        annonceStatus.save()
        # Créer l'embauche
        embauche = Embauche.objects.create(
            annonce=annonce,
            candidat=candidat,
            employe=employe
        )

        contrat_url = reverse("generer_contrat", args=[annonce.id, cv.id])
        redirect_url = reverse("candidats_annonce", args=[annonce.id])
        # Messages de succès
        messages.success(
            request, 
            f'Candidat {candidat.prenom} {candidat.nom} recruté avec succès!'
        )

        # Template avec téléchargement automatique + redirection
        return render(request, "rh/recrutement_done.html", {
            "annonce": annonce,
            "candidat": candidat,
            "employe": employe,
            "contrat_url": contrat_url,
            "redirect_url": redirect_url
        })
