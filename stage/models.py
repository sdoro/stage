
from django.db import models

class studente (models.Model):
        matricola = models.CharField(primary_key=True, max_length=20)
        cognome = models.CharField(max_length=30)
        nome = models.CharField(max_length=30)
        data_nascita = models.DateField(null=False)

	class Meta:
                verbose_name_plural = "Studenti"
	def __unicode__(self):
                return u"%s %s" % (self.nome, self.cognome)

class classe (models.Model):
        corso = models.CharField(max_length=20)
        anno_scolastico = models.CharField(max_length=9)
        referente = models.CharField(max_length=30)
        specializzazione = models.CharField(max_length=30)

	class Meta:
                verbose_name_plural = "Classi"
	def __unicode__(self):
                return u"%s %s %s" % (self.corso, self.anno_scolastico, self.specializzazione)


class azienda (models.Model):
        P_IVA = models.CharField(primary_key=True, max_length=11)
        denominazione = models.CharField(max_length=30)
        settore_merceologico = models.CharField(max_length=30)
        localita = models.CharField(max_length=30)
        tutor = models.CharField(max_length=30)

	class Meta:
                verbose_name_plural = "Aziende"
	def __unicode__(self):
                return u"%s %s" % (self.denominazione, self.localita)


class formazione (models.Model):
        matricola = models.ForeignKey(studente)
        P_IVA = models.ForeignKey(azienda)
        data_inizio = models.DateField()
        data_fine = models.DateField()
        argomento = models.CharField(max_length=30)
        valutazione = models.CharField(max_length=30)
        modo_di_svolgimento = models.CharField(max_length=30)

	class Meta:
                verbose_name_plural = "Formazioni"
	def __unicode__(self):
                return u"da %s a %s presso %s" % (self.data_inizio, self.data_fine, self.denominazione)

class frequenza (models.Model):
        matricola = models.ForeignKey(studente)
        corso = models.ForeignKey(classe, related_name='+')
        anno_scolastico = models.ForeignKey(classe, related_name='+')

	class Meta:
                verbose_name_plural = "Frequenze"

