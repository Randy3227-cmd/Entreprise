from django.shortcuts import get_object_or_404, render
from blog.models import (
    Annonce, AnnonceCompetence, AnnonceLangue, AnnonceFormation, CV, AnnonceLoisir
)
def score_cv(cv, annonce):
    score = 0

    if cv.statut.id == 2:
        score += 100
    elif cv.statut.id == 1:
        score += 10

    formations_obligatoires = AnnonceFormation.objects.filter(
        annonce=annonce, est_obligatoire=False
    ).values_list("formation_id", flat=True)

    formations_cv = cv.formations.all().values_list("formation_id", flat=True)
    score += sum(5 for f in formations_obligatoires if f in formations_cv)

    competences_demandees = AnnonceCompetence.objects.filter(
        annonce=annonce, est_obligatoire=False
    ).values_list("competence_id", flat=True)

    competences_cv = cv.competences.all().values_list("competence_id", flat=True)
    score += sum(3 for c in competences_demandees if c in competences_cv)

    langues_demandees = AnnonceLangue.objects.filter(
        annonce=annonce, est_obligatoire=False
    ).values_list("langue_id", flat=True)

    langues_cv = cv.langues.all().values_list("langue_id", flat=True)
    score += sum(3 for l in langues_demandees if l in langues_cv)

    loisirs_demandees = AnnonceLoisir.objects.filter(
        annonce=annonce, est_obligatoire=False
    ).values_list("loisir_id", flat=True)

    loisirs_cv = cv.loisirs.all().values_list("loisir_id", flat=True)
    score += sum(1 for l in loisirs_demandees if l in loisirs_cv)

    return score

