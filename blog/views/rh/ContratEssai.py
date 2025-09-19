from django.http import HttpResponse
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from blog.models import Candidat, Annonce, CV, Employe
import datetime


def generer_contrat(request, annonce_id, cv_id):
    annonce = Annonce.objects.get(id=annonce_id)
    cv = CV.objects.get(id=cv_id)
    candidat = cv.candidat
    employe = Employe.objects.filter(candidat=candidat).first()  

    # Réponse HTTP
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="contrat_{candidat.nom}_{candidat.prenom}.pdf"'

    # Document
    doc = SimpleDocTemplate(response, pagesize=A4,
                            rightMargin=50, leftMargin=50,
                            topMargin=50, bottomMargin=50)

    styles = getSampleStyleSheet()
    style_normal = styles['Normal']
    style_title = ParagraphStyle('Title', parent=styles['Heading1'], alignment=1, fontSize=14, spaceAfter=20)

    elements = []

    # Titre
    elements.append(Paragraph("CONTRAT DE TRAVAIL A DUREE INDETERMINEE", style_title))
    elements.append(Spacer(1, 20))

    # Partie introductive
    intro = f"""
    Entre Société XXXX, registre de commerce n°YYYYY, sis au lot XXXXX,
    représentée par son Directeur Général Monsieur XXXX, appelé ci-après l’Employeur,
    <br/><br/>
    Et <br/><br/>
    Monsieur <b>{candidat.nom} {candidat.prenom}</b>,<br/>
    Né le {candidat.date_naissance.strftime("%d/%m/%Y") if candidat.date_naissance else "____"},<br/>
    Résidant au {candidat.adresse if candidat.adresse else "____"},<br/>
    appelé ci-après l’Employé.
    """
    elements.append(Paragraph(intro, style_normal))
    elements.append(Spacer(1, 20))

    # Infos Annonce
    infos = f"""
    Date d’embauche : {datetime.date.today().strftime("%d/%m/%Y")}<br/>
    Durée de la période d’essai : 3 mois renouvelable une fois.<br/>
    Fonction : {annonce.role}<br/>
    Position : Cadre<br/>
    Rémunération brute : {employe.salaire if employe and employe.salaire else "____"} MGA<br/>
    Lieu du poste : {annonce.lieu_de_poste if annonce.lieu_de_poste else "____"}<br/>
    """
    elements.append(Paragraph(infos, style_normal))
    elements.append(Spacer(1, 20))

    # Articles
    articles = [
        "Art 1 Durant la période d’essai, le contrat pourrait être résilié par l’une ou l’autre partie, sans préavis ni indemnité...",
        "Art 2 L’employé s’engage à accepter les missions qui lui sont confiées...",
        "Art 3 L’employeur se réserve le droit, après concertation avec l’employé, de modifier les fonctions...",
        "Art 4 L’avancement de l’employé sera fonction des procédures en vigueur...",
        "Art 5 L’évaluation de l’employé se fera au moins une fois par an...",
        "Art 6 L’employé s’engage à respecter les règles de déontologie...",
        "Art 7 L’Employé doit toute son activité professionnelle à son Employeur...",
        "Art 8 Toute faute professionnelle peut entraîner un licenciement immédiat...",
        "Art 9 La durée du travail, le droit aux congés payés, le régime de retraite...",
        "Art 10 L’employé doit remettre à l’employeur l’ensemble des pièces justificatives...",
        "Art 11 Tout autre point non mentionné dans ce présent contrat sera régi par les lois en vigueur.",
        "Art 12 Tout différend né de l’interprétation ou de l’application du présent contrat sera porté devant le Tribunal du Travail d’Antananarivo."
    ]

    for art in articles:
        elements.append(Paragraph(art, style_normal))
        elements.append(Spacer(1, 12))

    # Signature
    today = datetime.date.today().strftime("%d/%m/%Y")
    signature = f"""
    Fait à Antananarivo, le {today}.<br/><br/>
    En double exemplaire<br/><br/>
    L’Employeur&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;L’Employé<br/><br/>
    (mention manuscrite : lu et approuvé)
    """
    elements.append(Spacer(1, 30))
    elements.append(Paragraph(signature, style_normal))

    # Build PDF
    doc.build(elements)
    return response
