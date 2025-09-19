from django.db import models


class Employe(models.Model):
    salaire = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    candidat = models.OneToOneField("Candidat", on_delete=models.CASCADE)
    poste = models.ForeignKey("Poste", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.candidat.nom} {self.candidat.prenom} - {self.poste.nom}"


class Embauche(models.Model):
    annonce = models.ForeignKey("Annonce", on_delete=models.CASCADE)
    candidat = models.ForeignKey("Candidat", on_delete=models.CASCADE)
    employe = models.ForeignKey("Employe", on_delete=models.CASCADE)
    date_changement = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Embauche de {self.candidat.nom} {self.candidat.prenom} pour {self.annonce.role}"


class StatutEmploye(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom


class HistoriqueStatutEmploye(models.Model):
    employe = models.ForeignKey("Employe", on_delete=models.CASCADE)
    statut = models.ForeignKey("StatutEmploye", on_delete=models.CASCADE)
    date_changement = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employe} -> {self.statut.nom} ({self.date_changement})"
