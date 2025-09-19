from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from blog.views.rh.AnnonceForm import creer_annonce  # import depuis ton sous-dossier
from blog.views.rh.AnnonceListeRh import liste_annonces  # import depuis ton sous-dossier
from blog.views.rh.AnnonceListeRh import liste_annoncesCandidat  # import depuis ton sous-dossier
from blog.views.rh.AnnonceListeRh import detail_annonceCandidat  # import depuis ton sous-dossier
from blog.views.rh.Postuler import postuler  # import depuis ton sous-dossier
from blog.views.rh.AnnonceListeRh import detail_annonceRh  # import depuis ton sous-dossier
from blog.views.rh.AnnonceListeRh import candidats_annonce  # import depuis ton sous-dossier
from blog.views.rh.Accueil import *
from blog.views.rh.qcm import *
from blog.views.rh.Recruter import recruter
from blog.views.rh.ClassifierCV import classifier_cv

urlpatterns = [
    path('', accueil, name='acceuil'),
    path('rh/login/', rh_login, name='rh_login'),
    path('rh/besoin/saisie', creer_annonce, name='creer_annonce'),
    path('rh/annonce/liste', liste_annonces, name='liste_annonces'),
    path('candidat/annonce/liste', liste_annoncesCandidat, name='liste_annoncesCandidat'),
    path('rh/annonce/<int:annonce_id>/', detail_annonceRh, name='detail_annonceRh'),
    path('candidat/annonce/<int:annonce_id>/', detail_annonceCandidat, name='detail_annonceCandidat'),
    path('candidat/annonce/<int:annonce_id>/postuler/', postuler, name='postuler'),
    path('rh/contrat/generer/<int:annonce_id>/<int:cv_id>/', views.generer_contrat, name='generer_contrat'),
    path('rh/annonce/<int:annonce_id>/candidats/', candidats_annonce, name='candidats_annonce'),
    path('candidat/test/<int:annonce_id>/<int:candidat_id>/', showQCM, name='showQCM'),
    path('candidat/test/score', score_test, name='score_test'),
    path('rh/recruter/<int:annonce_id>/', recruter, name='recruter'),
    path('candidat/cv/classifier/<int:annonce_id>/', classifier_cv, name='classifier_cv'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)