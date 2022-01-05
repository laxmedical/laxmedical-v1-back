from typing import DefaultDict
from django.db import models
from django.contrib.auth.models  import  User

class Patient(models.Model):
    editor     = models.ForeignKey(User, on_delete=models.CASCADE)   # la liaison onToOn vers le modèle User
    #user      = models.OneToOneField(User, related_name="patient", on_delete=models.CASCADE)
    
    username   = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    #avatar    = models.ImageField(null=True, blank=True, upload_to="patients/avatars/")
    
    options = (
        ('M', 'M'),
        ('F', 'F'),
    )
    sex        = models.CharField(max_length=1, choices=options, default='M')
    blud_group = models.CharField(max_length=1, choices=options, default='M')
    birth_date = models.DateField(null=True)
    adress     = models.TextField(max_length=200, null=True)
    
    is_dead    = models.BooleanField(default=False)
    data       = models.JSONField(null=True)

    def __unicode__(self):
        return  u"Profil patient de {0}".format(self.username)
    
    def __str__(self):
        return  u"Profil patient de {0}".format(self.username)


class Fiche(models.Model):
    editor      = models.ForeignKey(User,related_name="fiches", on_delete=models.SET_NULL, null=True)
    patient     = models.ForeignKey(Patient, related_name="fiches", on_delete=models.SET_NULL, null=True) 
    date        = models.DateTimeField(auto_now_add=True)
    
    poid        = models.FloatField(null=True)
    temperature = models.IntegerField(null=True)
    description = models.TextField(null=True)
    
    is_urgent   = models.BooleanField(default=False)
    type        = models.CharField(default=None, max_length=100)

    def __str__(self):
        return  u"Fiche de {0}".format(self.patient.username)
    
    
class Consultation(models.Model):
    editor      = models.ForeignKey(User,related_name="consultations", on_delete=models.SET_NULL, null=True)
    fiche       = models.ForeignKey(Fiche, related_name="consultations", on_delete=models.SET_NULL, null=True) 
    date        = models.DateTimeField(auto_now_add=True)
    
    type        = models.CharField(default=None, max_length=100)
    data        = models.JSONField(null=True)

    def __str__(self):
        return  u"Consultation de {0}".format(self.fiche.pk)
 
       
class Ordonnace(models.Model):
    editor      = models.ForeignKey(User,related_name="ordonnaces", on_delete=models.SET_NULL, null=True)
    fiche       = models.ForeignKey(Fiche, related_name="ordonnaces", on_delete=models.SET_NULL, null=True) 
    date        = models.DateTimeField(auto_now_add=True)
    
    type        = models.CharField(default=None, max_length=100)
    data        = models.JSONField(null=True)

    def __str__(self):
        return  u"Ordonnace de {0}".format(self.fiche.pk)
       
class Prelevement(models.Model):
    editor      = models.ForeignKey(User,related_name="prelevements", on_delete=models.SET_NULL, null=True)
    fiche       = models.ForeignKey(Fiche, related_name="prelevements", on_delete=models.SET_NULL, null=True) 
    date        = models.DateTimeField(auto_now_add=True)
    
    type        = models.CharField(default=None, max_length=100)
    data        = models.JSONField(null=True)

    def __str__(self):
        return  u"prelevement de {0}".format(self.fiche.pk)
    
class Soin(models.Model):
    editor      = models.ForeignKey(User,related_name="soins", on_delete=models.SET_NULL, null=True)
    fiche       = models.ForeignKey(Fiche, related_name="soins", on_delete=models.SET_NULL, null=True) 
    date        = models.DateTimeField(auto_now_add=True)
    
    type        = models.CharField(default=None, max_length=100)
    data        = models.JSONField(null=True)

    def __str__(self):
        return  u"Soin de {0}".format(self.fiche.pk)
       
class BonAnalyse(models.Model):
    editor      = models.ForeignKey(User,related_name="bon_analyses", on_delete=models.SET_NULL, null=True)
    consultation= models.ForeignKey(Consultation, related_name="bon_analyses", on_delete=models.SET_NULL, null=True) 
    date        = models.DateTimeField(auto_now_add=True)
    
    type        = models.CharField(default=None, max_length=100)
    data        = models.JSONField(null=True)

    def __str__(self):
        return  u"bon_analyse n° {0}".format(self.pk)
       
class Analyse(models.Model):
    editor      = models.ForeignKey(User,related_name="analyses", on_delete=models.SET_NULL, null=True)
    bon_analyse = models.ForeignKey(BonAnalyse, related_name="analyses", on_delete=models.SET_NULL, null=True) 
    date        = models.DateTimeField(auto_now_add=True)
    
    type        = models.CharField(default=None, max_length=100)
    analyses    = models.JSONField(null=True)
    results     = models.JSONField(null=True)

    def __str__(self):
        return  u"Ordonnace de {0}".format(self.fiche.pk)
       
class Hospitalisation(models.Model):
    editor      = models.ForeignKey(User,related_name="hospitalisations", on_delete=models.SET_NULL, null=True)
    fiche       = models.ForeignKey(Fiche, related_name="hospitalisations", on_delete=models.SET_NULL, null=True) 
    date        = models.DateTimeField(auto_now_add=True)
    start_date  = models.DateTimeField()
    end_date    = models.DateTimeField()
    
    type        = models.CharField(default=None, max_length=100)
    data        = models.JSONField(null=True)

    def __str__(self):
        return  u"Ordonnace de {0}".format(self.fiche.pk)
       
class Operation(models.Model):
    editor      = models.ForeignKey(User,related_name="operations", on_delete=models.SET_NULL, null=True)
    fiche       = models.ForeignKey(Fiche, related_name="operations", on_delete=models.SET_NULL, null=True) 
    date        = models.DateTimeField(auto_now_add=True)
    
    type        = models.CharField(default=None, max_length=100)
    data        = models.JSONField(null=True)

    def __str__(self):
        return  u"Ordonnace de {0}".format(self.fiche.pk)
    
    
class FactureGrid(models.Model):
    editor      = models.ForeignKey(User,related_name="facture_grids", on_delete=models.SET_NULL, null=True)
    date        = models.DateTimeField(auto_now_add=True)
    
    type        = models.CharField(default=None, max_length=100)
    data        = models.JSONField(null=True)

    def __str__(self):
        return  u"FactureGrid de {0}".format(self.editor.username)
    
class Facture(models.Model):
    editor      = models.ForeignKey(User,related_name="factures", on_delete=models.SET_NULL, null=True)
    date        = models.DateTimeField(auto_now_add=True)
    
    type        = models.CharField(default=None, max_length=100)
    data        = models.JSONField(null=True)

    def __str__(self):
        return  u"Facture de {0}".format(self.editor.username)
    
          
class Alert(models.Model):
    editor      = models.ForeignKey(User,related_name="alerts", on_delete=models.SET_NULL, null=True)
    date        = models.DateTimeField(auto_now_add=True)
    
    type        = models.CharField(default=None, max_length=100)
    data        = models.JSONField(null=True)

    def __str__(self):
        return  u"alert de {0}".format(self.editor.username)
    
    
class WorkplaceSetting(models.Model):
    user        = models.ForeignKey(User,related_name="workplace_settings", on_delete=models.SET_NULL, null=True)
    date        = models.DateTimeField(auto_now_add=True)
    
    type        = models.CharField(default=None, max_length=100)
    data        = models.JSONField(null=True)

    def __str__(self):
        return  u"alert de {0}".format(self.editor.username)
