from django.db import models

class Formation(models.Model):
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description


class Competence(models.Model):
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description


class Langue(models.Model):
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description


class Loisir(models.Model):
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description
