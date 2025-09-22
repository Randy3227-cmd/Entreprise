from django.shortcuts import render
from blog.models.rh.Annonce import *
from blog.models.rh.Candidat import *
from blog.models.rh.rh import AnnonceStatus
from django.shortcuts import get_object_or_404
from django.utils import timezone
def liste_annonces(request):
    # Récupère toutes les annonces avec le poste associé
    annonces = Annonce.objects.select_related('poste').all().order_by('-date_limite_postule')
    #Filtre les annonces dont le statut est True (fermées)
    annonces = [annonce for annonce in annonces if not AnnonceStatus.objects.filter(annonce=annonce, status=True).exists()]
    return render(request, 'rh/liste_annoncesRh.html', {'annonces': annonces})

def liste_annoncesCandidat(request):
    now = timezone.now()
    # Récupère toutes les annonces avec le poste associé
    annonces = Annonce.objects.select_related('poste').all().order_by('-date_limite_postule')
    
    # Filtre les annonces fermées ou dont la date limite est dépassée
    annonces = [
        annonce for annonce in annonces
        if not AnnonceStatus.objects.filter(annonce=annonce, status=True).exists()
        and annonce.date_limite_postule and annonce.date_limite_postule > now
    ]
    
    return render(request, 'rh/liste_annonceCandidat.html', {'annonces': annonces})

def detail_annonceCandidat(request, annonce_id):
    annonce = get_object_or_404(Annonce, id=annonce_id)
    
    # Récupérer les relations (formations, compétences, langues, loisirs, CV)
    formations = annonce.annonceformation_set.all()
    competences = annonce.annoncecompetence_set.all()
    langues = annonce.annoncelangue_set.all()
    loisirs = annonce.annonceloisir_set.all()
    cvs = annonce.annoncecv_set.all()
    
    context = {
        'annonce': annonce,
        'formations': formations,
        'competences': competences,
        'langues': langues,
        'loisirs': loisirs,
        'cvs': cvs,
    }
    return render(request, 'rh/detail_annonceCandidat.html', context)
def detail_annonceRh(request, annonce_id):
    annonce = get_object_or_404(Annonce, id=annonce_id)
    
    # Récupérer les relations (formations, compétences, langues, loisirs, CV)
    formations = annonce.annonceformation_set.all()
    competences = annonce.annoncecompetence_set.all()
    langues = annonce.annoncelangue_set.all()
    loisirs = annonce.annonceloisir_set.all()
    cvs = annonce.annoncecv_set.all()
    
    context = {
        'annonce': annonce,
        'formations': formations,
        'competences': competences,
        'langues': langues,
        'loisirs': loisirs,
        'cvs': cvs,
    }
    return render(request, 'rh/detail_annonceRh.html', context)
def candidats_annonce(request, annonce_id):
    annonce = get_object_or_404(Annonce, id=annonce_id)

    # Récupère tous les CV liés à cette annonce
    cvs = CV.objects.filter(annoncecv__annonce=annonce).distinct()
    has_recrute = cvs.filter(statut__description__iexact='Recrute').exists()

    context = {
        "annonce": annonce,
        "cvs": cvs,
        "statut": has_recrute,
    }
    return render(request, "rh/candidats_annonce.html", context)