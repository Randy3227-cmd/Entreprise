from django.shortcuts import render, redirect
from blog.models.rh.rh import *
from blog.models.rh.Annonce import *
from blog.models.rh.Candidat import *
from django.shortcuts import get_object_or_404
from datetime import date, timedelta

def showQCM(request, annonce_id, candidat_id):
    # Récupérer l'annonce
    annonce = get_object_or_404(Annonce, id=annonce_id) 
    candidat = get_object_or_404(Candidat, id=candidat_id)

    # Récupérer le poste associé
    poste = annonce.poste
    poste_id = poste.id

    # Récupérer le test lié au poste
    test_poste = TestPoste.objects.filter(id_poste=poste_id).first()
    if not test_poste:
        context = {'annonce': annonce, 'poste': poste, 'questions': []}
        return render(request, 'qcm_template.html', context)

    test = test_poste.id_test  # objet Test

    # Récupérer les questions du test
    test_questions = TestQuestion.objects.filter(id_test=test)

    questions_list = []
    for tq in test_questions:
        question = tq.id_question  # objet Question

        # Toutes les réponses possibles pour cette question
        reponses = QuestionReponse.objects.filter(id_question=question)
        reponses_data = [{'id': r.id_reponse.id, 'texte': r.id_reponse.reponse} for r in reponses]

        questions_list.append({
            'id': question.id,
            'texte': question.question,
            'point': question.point,
            'reponses': reponses_data
        })

    context = {
        'annonce': annonce,
        'poste': poste,
        'test': test,
        'questions': questions_list,
        'candidat_id': candidat.id,
    }

    return render(request, 'rh/qcm_template.html', {'test' : context})

def score_test(request):
    if request.method == "POST":
        annonce_id = request.POST.get("annonce_id")
        candidat_id = request.POST.get("candidat_id")
        
        annonce = get_object_or_404(Annonce, id=annonce_id)
        candidat = get_object_or_404(Candidat, id=candidat_id)
        date_entretien = date.today() + timedelta(days=5)
    
        try:
            cv = CV.objects.get(candidat=candidat, annoncecv__annonce=annonce)
        except CV.DoesNotExist:
            cv = None
        
        poste = annonce.poste
        test_poste = TestPoste.objects.filter(id_poste=poste).first()
        if not test_poste:
            return render(request, "rh/qcm_template.html", {"test": None})

        test = test_poste.id_test
        test_questions = TestQuestion.objects.filter(id_test=test)

        total_points = 0
        points_obtenus = 0
        resultats = []

        for tq in test_questions:
            question = tq.id_question
            total_points += question.point or 0

            reponse_id = request.POST.get(f"question_{question.id}")
            try:
                reponse = Reponse.objects.get(id=reponse_id)
                texte_reponse = reponse.reponse
            except (Reponse.DoesNotExist, TypeError):
                texte_reponse = None
                reponse_id = None

            if not reponse_id:
                resultats.append({
                    "question": question.question,
                    "reponse_donnee": None,
                    "correcte": False,
                })
                ScoreQuestion.objects.create(
                    note=0,
                    id_question=question,
                    id_test=test,
                    id_candidat=candidat,
                    id_annonce=annonce
                )
                continue

            bonne_reponse = CorrectReponse.objects.filter(
                id_question=question, id_reponse=reponse_id
            ).exists()

            note_obtenue = question.point if bonne_reponse else 0
            if bonne_reponse:
                points_obtenus += question.point or 0

            ScoreQuestion.objects.create(
                note=note_obtenue,
                id_question=question,
                id_test=test,
                id_candidat=candidat,
                id_annonce=annonce
            )

            resultats.append({
                "question": question.question,
                "reponse_donnee": texte_reponse,
                "correcte": bonne_reponse,
            })

        score = {
            "total": total_points,
            "obtenus": points_obtenus,
            "pourcentage": round((points_obtenus / total_points) * 100, 2) if total_points else 0,
        }

        decision = 0
        if points_obtenus < 6: 
            decision = 1

        if decision == 0:
            PlanningEntretien.objects.create(
                date_entretien=date_entretien,
                id_candidat=candidat,
                id_annonce=annonce
            )

            cv.statut = StatutCV.objects.get(description='Test valide')
            cv.save()

        context = {
            "annonce": annonce,
            "poste": poste,
            "test": test,
            "resultats": resultats,
            "score": score,
            "decision": decision,
            "candidat": candidat,
            "date_entretien": date_entretien,
        }

        return render(request, "rh/resultat_test.html", context)
