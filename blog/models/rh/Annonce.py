from django.db import models

class Poste(models.Model):
    nom = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nom
    
class Annonce(models.Model):
    role = models.CharField(max_length=150)  
    salaire = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    horaire_de_travail = models.IntegerField(blank=True, null=True)  
    lieu_de_poste = models.CharField(max_length=255, blank=True, null=True)
    date_limite_postule = models.DateTimeField(blank=True, null=True)
    document_necessaire = models.CharField(max_length=255, blank=True, null=True)
    poste = models.ForeignKey('Poste', on_delete=models.CASCADE, related_name='annonces') 

    def __str__(self):
        return self.role
    
class AnnonceFormation(models.Model):
    annonce = models.ForeignKey("Annonce", on_delete=models.CASCADE)
    formation = models.ForeignKey("Formation", on_delete=models.CASCADE)
    est_obligatoire = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.annonce} - {self.formation}"


class AnnonceCompetence(models.Model):
    annonce = models.ForeignKey("Annonce", on_delete=models.CASCADE)
    competence = models.ForeignKey("Competence", on_delete=models.CASCADE)
    est_obligatoire = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.annonce} - {self.competence}"


class AnnonceLangue(models.Model):
    annonce = models.ForeignKey("Annonce", on_delete=models.CASCADE)
    langue = models.ForeignKey("Langue", on_delete=models.CASCADE)
    est_obligatoire = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.annonce} - {self.langue}"


class AnnonceLoisir(models.Model):
    annonce = models.ForeignKey("Annonce", on_delete=models.CASCADE)
    loisir = models.ForeignKey("Loisir", on_delete=models.CASCADE)
    est_obligatoire = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.annonce} - {self.loisir}"


class AnnonceCV(models.Model):
    annonce = models.ForeignKey("Annonce", on_delete=models.CASCADE)
    cv = models.ForeignKey("CV", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.annonce} - {self.cv}"
    
    
class AnnonceStatus(models.Model):
    annonce = models.ForeignKey(Annonce, on_delete=models.CASCADE, db_column='id_annonce')
    status = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'annonce_status'