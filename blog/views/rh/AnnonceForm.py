from django.shortcuts import render, redirect
from blog.models import (
    Annonce, Poste, Competence, Langue, Loisir, Formation,
    AnnonceCompetence, AnnonceLangue, AnnonceLoisir, AnnonceFormation
)

def creer_annonce(request):
    # Récupérer toutes les données existantes pour les sélections
    postes = Poste.objects.all()
    competences = Competence.objects.all()
    langues = Langue.objects.all()
    loisirs = Loisir.objects.all()
    formations = Formation.objects.all()

    if request.method == "POST":
        # Données principales
        role = request.POST.get("role")
        salaire = request.POST.get("salaire") or None
        horaire = request.POST.get("horaire_de_travail") or None
        lieu = request.POST.get("lieu_de_poste")
        date_limite = request.POST.get("date_limite_postule") or None
        doc = request.POST.get("document_necessaire")
        id_poste = request.POST.get("poste")
        
        # Création de l'annonce
        annonce = Annonce.objects.create(
            role=role,
            salaire=salaire,
            horaire_de_travail=horaire,
            lieu_de_poste=lieu,
            date_limite_postule=date_limite,
            document_necessaire=doc,
            poste_id=id_poste
        )

        # Fonction pour traiter chaque catégorie
        def process_items(model, key_prefix):
            selected_ids = request.POST.getlist(f"{key_prefix}_ids[]")
            obligatory_ids = request.POST.getlist(f"{key_prefix}_obligatoire[]")

            for item in selected_ids:
                # Vérifie si c'est un ID existant ou un nouveau tag
                try:
                    obj = model._meta.get_field(key_prefix).related_model.objects.get(id=int(item))
                except ValueError:
                    # Nouveau tag => création ou récupération si déjà existant
                    obj_model = model._meta.get_field(key_prefix).related_model
                    obj, created = obj_model.objects.get_or_create(description=item)

                # Vérifie si la relation existe déjà pour cette annonce
                relation_exists = model.objects.filter(annonce=annonce, **{key_prefix: obj}).exists()
                if not relation_exists:
                    model.objects.create(
                        annonce=annonce,
                        **{key_prefix: obj},
                        est_obligatoire=str(obj.id) in obligatory_ids
                    )

        # Traiter toutes les catégories
        process_items(AnnonceCompetence, "competence")
        process_items(AnnonceLangue, "langue")
        process_items(AnnonceLoisir, "loisir")
        process_items(AnnonceFormation, "formation")

        return redirect("creer_annonce")  # ou vers une page détail si tu en as une

    # Préparer le contexte pour l'affichage du formulaire
    champs = [
        ('competence', competences),
        ('langue', langues),
        ('loisir', loisirs),
        ('formation', formations),
    ]
    context = {
        "postes": postes,
        "champs": champs,
    }
    return render(request, 'rh/creer_annonce.html', context)
