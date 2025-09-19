from django.shortcuts import get_object_or_404, render
from blog.models import (
    Annonce, CV,
)
from blog.utils.ClassificationCV import score_cv

def classifier_cv(request, annonce_id):
    annonce = get_object_or_404(Annonce, id=annonce_id)

    cvs = CV.objects.filter(annoncecv__annonce=annonce)

    cvs_scores = [(cv, score_cv(cv, annonce)) for cv in cvs]
    cvs_scores.sort(key=lambda x: x[1], reverse=True) 

    return render(request, "rh/classement.html", {
        "annonce": annonce,
        "cvs_scores": cvs_scores,
    })
