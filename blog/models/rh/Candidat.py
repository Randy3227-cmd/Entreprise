from django.db import models


class Candidat(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(max_length=150, unique=False)
    telephone = models.CharField(max_length=30, null=True, blank=True)
    date_naissance = models.DateField(null=True, blank=True)
    adresse = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return f"{self.prenom} {self.nom}"

class StatutCV(models.Model):
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description
    

class CV(models.Model):
    titre = models.CharField(max_length=150)
    resume = models.TextField(null=True, blank=True)
    date_creation = models.DateField(auto_now_add=True)
    candidat = models.ForeignKey(Candidat, on_delete=models.CASCADE, related_name="cvs")
    photo = models.ImageField(upload_to='photos_cv/', null=True, blank=True)
    statut = models.ForeignKey(StatutCV, on_delete=models.CASCADE, related_name="statut")
    cin = models.CharField(max_length=255, null=False, blank=False, unique=True)
    
    def __str__(self):
        return f"{self.titre} ({self.candidat})"


class CVFormation(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name="formations")
    formation = models.ForeignKey("Formation", on_delete=models.CASCADE)
    date_debut = models.DateField(null=True, blank=True)
    date_fin = models.DateField(null=True, blank=True)
    etablissement = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.cv} - {self.formation}"


class CVCompetence(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name="competences")
    competence = models.ForeignKey("Competence", on_delete=models.CASCADE)
    niveau = models.CharField(max_length=50, null=True, blank=True)  # ex: débutant, intermédiaire, expert

    def __str__(self):
        return f"{self.cv} - {self.competence} ({self.niveau})"


class CVLangue(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name="langues")
    langue = models.ForeignKey("Langue", on_delete=models.CASCADE)
    niveau = models.CharField(max_length=50, null=True, blank=True)  # ex: basique, courant, bilingue

    def __str__(self):
        return f"{self.cv} - {self.langue} ({self.niveau})"


class CVLoisir(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name="loisirs")
    loisir = models.ForeignKey("Loisir", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cv} - {self.loisir}"
