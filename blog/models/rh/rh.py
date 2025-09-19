# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from blog.models.rh.Annonce import *
from blog.models.rh.Candidat import *
from blog.models.rh.Criteres import *

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CorrectReponse(models.Model):
    id_question = models.ForeignKey('Question', models.DO_NOTHING, db_column='id_question')
    id_reponse = models.ForeignKey('Reponse', models.DO_NOTHING, db_column='id_reponse')

    class Meta:
        managed = False
        db_table = 'correct_reponse'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class PlanningEntretient(models.Model):
    date_entretien = models.DateField(blank=True, null=True)
    id_candidat = models.ForeignKey(Candidat, models.DO_NOTHING, db_column='id_candidat')

    class Meta:
        managed = False
        db_table = 'planning_entretient'

class Question(models.Model):
    question = models.CharField(max_length=255, blank=True, null=True)
    point = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'question'


class QuestionReponse(models.Model):
    id_question = models.ForeignKey(Question, models.DO_NOTHING, db_column='id_question')
    id_reponse = models.ForeignKey('Reponse', models.DO_NOTHING, db_column='id_reponse')

    class Meta:
        managed = False
        db_table = 'question_reponse'


class Reponse(models.Model):
    reponse = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reponse'


class ScoreEntretien(models.Model):
    note = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    id_annonce = models.ForeignKey(Annonce, models.DO_NOTHING, db_column='id_annonce')
    id_candidat = models.ForeignKey(Candidat, models.DO_NOTHING, db_column='id_candidat')

    class Meta:
        managed = False
        db_table = 'score_entretien'


class ScoreQuestion(models.Model):
    note = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    id_question = models.ForeignKey(Question, models.DO_NOTHING, db_column='id_question')
    id_test = models.ForeignKey('Test', models.DO_NOTHING, db_column='id_test')
    id_candidat = models.ForeignKey(Candidat, models.DO_NOTHING, db_column='id_candidat')
    id_annonce = models.ForeignKey(Annonce, models.DO_NOTHING, db_column='id_annonce')

    class Meta:
        managed = False
        db_table = 'score_question'


class ScoreTotal(models.Model):
    id_candidat = models.ForeignKey(Candidat, models.DO_NOTHING, db_column='id_candidat')
    id_annonce = models.ForeignKey(Annonce, models.DO_NOTHING, db_column='id_annonce')
    note = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'score_total'


class Test(models.Model):
    nom = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test'


class TestPoste(models.Model):
    id_test = models.ForeignKey(Test, models.DO_NOTHING, db_column='id_test')
    id_poste = models.ForeignKey(Poste, models.DO_NOTHING, db_column='id_poste')

    class Meta:
        managed = False
        db_table = 'test_poste'


class TestQuestion(models.Model):
    id_question = models.ForeignKey(Question, models.DO_NOTHING, db_column='id_question')
    id_test = models.ForeignKey(Test, models.DO_NOTHING, db_column='id_test')

    class Meta:
        managed = False
        db_table = 'test_question'