from django.shortcuts import render, get_object_or_404, redirect
from blog.models.rh.Annonce import *
from blog.models.rh.Candidat import * 
from blog.models.rh.Employe import *

def recruter(request, annonce_id):
    annonce = get_object_or_404(Annonce, id=annonce_id)

    if request.method == "POST":
        candidat_id = request.POST.get("candidat_id")
        salaire = request.POST.get("salaire")
        poste_id = annonce.poste.id  # Utiliser le poste de l'annonce

        candidat = get_object_or_404(Candidat, id=candidat_id)

        # Créer l'employé
        employe = Employe.objects.create(
            salaire=salaire,
            candidat=candidat,
            poste_id=poste_id
        )

        # Créer l'embauche
        Embauche.objects.create(
            annonce=annonce,
            candidat=candidat,
            employe=employe
        )

        return redirect("liste_annonces")

    return render(request, "rh/recruter.html", {
        "annonce": annonce
    })