from django.shortcuts import render, get_object_or_404, redirect
from blog.models.rh.Candidat import *
from blog.models.rh.Annonce import *
from blog.models.rh.Criteres import *


def cv_passe_test(cv, annonce):
    formations_obligatoires = AnnonceFormation.objects.filter(
        annonce=annonce, est_obligatoire=True
    ).values_list("formation_id", flat=True)

    for f_id in formations_obligatoires:
        if not cv.formations.filter(formation_id=f_id).exists():
            return False

    competences_obligatoires = AnnonceCompetence.objects.filter(
        annonce=annonce, est_obligatoire=True
    ).values_list("competence_id", flat=True)

    for c_id in competences_obligatoires:
        if not cv.competences.filter(competence_id=c_id).exists():
            return False

    langues_obligatoires = AnnonceLangue.objects.filter(
        annonce=annonce, est_obligatoire=True
    ).values_list("langue_id", flat=True)

    for l_id in langues_obligatoires:
        if not cv.langues.filter(langue_id=l_id).exists():
            return False

    loisirs_obligatoires = AnnonceLoisir.objects.filter(
        annonce=annonce, est_obligatoire=True
    ).values_list("loisir_id", flat=True)

    for lo_id in loisirs_obligatoires:
        if not cv.loisirs.filter(loisir_id=lo_id).exists():
            return False

    return True

def postuler(request, annonce_id):
    annonce = get_object_or_404(Annonce, id=annonce_id)
    test = None

    champs = {
        "competences": Competence.objects.all(),
        "langues": Langue.objects.all(),
        "loisirs": Loisir.objects.all(),
        "formations": Formation.objects.all(),
    }

    if request.method == "POST":
        candidat = Candidat.objects.create(
            nom=request.POST.get("nom"),
            prenom=request.POST.get("prenom"),
            email=request.POST.get("email"),
            telephone=request.POST.get("telephone"),
            date_naissance=request.POST.get("date_naissance") or None,
            adresse=request.POST.get("adresse"),
            cin=request.POST.get("cin")
        )

        statut = get_object_or_404(StatutCV, id=1)

        cv = CV.objects.create(
            titre=request.POST.get("titre"),
            resume=request.POST.get("resume"),
            candidat=candidat,
            photo=request.FILES.get("photo"),
            statut=statut,
        )

        AnnonceCV.objects.create(annonce=annonce, cv=cv)

        for formation_id in request.POST.getlist("formations_ids[]"):
            if formation_id:
                try:
                    formation_obj = Formation.objects.get(id=int(formation_id))
                except ValueError:
                    formation_obj, _ = Formation.objects.get_or_create(description=formation_id)

                CVFormation.objects.create(
                    cv=cv,
                    formation=formation_obj,
                    date_debut=request.POST.get(f"date_debut_{formation_id}") or None,
                    date_fin=request.POST.get(f"date_fin_{formation_id}") or None,
                    etablissement=request.POST.get(f"etablissement_{formation_id}") or ""
                )

        for competence_id in request.POST.getlist("competences_ids[]"):
            if competence_id:
                try:
                    competence_obj = Competence.objects.get(id=int(competence_id))
                except ValueError:
                    competence_obj, _ = Competence.objects.get_or_create(description=competence_id)

                CVCompetence.objects.create(
                    cv=cv,
                    competence=competence_obj,
                    niveau=request.POST.get(f"niveau_competences_{competence_id}") or ""
                )

        for langue_id in request.POST.getlist("langues_ids[]"):
            if langue_id:
                try:
                    langue_obj = Langue.objects.get(id=int(langue_id))
                except ValueError:
                    langue_obj, _ = Langue.objects.get_or_create(description=langue_id)

                CVLangue.objects.create(
                    cv=cv,
                    langue=langue_obj,
                    niveau=request.POST.get(f"niveau_langues_{langue_id}") or ""
                )

        for loisir_id in request.POST.getlist("loisirs_ids[]"):
            if loisir_id:
                try:
                    loisir_obj = Loisir.objects.get(id=int(loisir_id))
                except ValueError:
                    loisir_obj, _ = Loisir.objects.get_or_create(description=loisir_id)

                CVLoisir.objects.create(
                    cv=cv,
                    loisir=loisir_obj
                )

        if cv_passe_test(cv, annonce):
            cv.statut = get_object_or_404(StatutCV, id=2) 
            cv.save()
            return redirect("showQCM", annonce_id, candidat.id)
        # else:
        #     cv.statut = get_object_or_404(StatutCV, id=2) 

        return redirect("liste_annoncesCandidat")

    context = {
        "annonce": annonce,
        "champs": champs.items(),
        "test" : test 
    }

    return render(request, "rh/postuler.html", context)

