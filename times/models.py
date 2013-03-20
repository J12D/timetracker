# -*- coding: utf-8 -*-
from django.db import models
import datetime

class Submission(models.Model):
  sub_date = models.DateTimeField('Meldedatum')
  time = models.DecimalField('Zeit gearbeitet', max_digits=5, decimal_places=2)
  comment = models.TextField('Beschreibung')
  NAME_CHOICES = (
    ("Alexander Schilbach", "Alexander Schilbach"),
    ("Bastian Enking", "Bastian Enking"),
    ("Benedikt Schuler", "Benedikt Schuler"),
    ("Caroline Grabellus", "Caroline Grabellus"),
    ("Christopher Leinkauf", "Christopher Leinkauf"),
    ("David Beul", "David Beul"),
    ("Denis Weiss", "Denis Weiss"),
    ("Dominik Holste", "Dominik Holste"),
    ("Friedrich Holotiuk", "Friedrich Holotiuk"),
    ("Gianna Lange", "Gianna Lange"),
    ("Julian Debus",  "Julian Debus"),
    ("Lutz Koller", "Lutz Koller"),
    ("Marc Matthiae", "Marc Matthiae"),
    ("Matthias Lehnen", "Matthias Lehnen"),
    ("Max Richter", "Max Richter"),
    ("Maximilian Jung", "Maximilian Jung"),
    ("Maximilian Plies", "Maximilian Plies"),
    ("Nicole Spakowski", "Nicole Spakowski"),
    ("Pascal Ohrisch", "Pascal Ohrisch"),
    ("Pascal Segesser", "Pascal Segesser"),
    ("Robin Jorda", "Robin Jorda"),
    ("Simon Pohl", "Simon Pohl"),
    ("Timo Sommerfeld", "Timo Sommerfeld"),
    ("Tobias Roediger", "Tobias Roediger"),
    ("Tobias Schlimpen", "Tobias Schlimpen"),
  )
  TASK_CHOICES = (
    ("Sonstiges","Sonstiges"),
    ("Definition Anlagestrategie","Definition Anlagestrategie"),
    (u"Präsentation Definition Anlagestrategie",u"Präsentation Definition Anlagestrategie"),
    ("Analyse klassischer Anlagestrategien","Analyse klassischer Anlagestrategien"),
    (u"Präsentation von klassischen Anlagestrategien",u"Präsentation von klassischen Anlagestrategien"),
    ("Definition Backtesting","Definition Backtesting"),
    (u"Präsentation Definition Backtesting",u"Präsentation Definition Backtesting"),
    ("Aufbau Zeiterfassungstool","Aufbau Zeiterfassungstool"),
    ("Aufbau Dokumenten Management System","Aufbau Dokumenten Management System"),
    ("Aufbau Project Management Tool","Aufbau Project Management Tool"),
    (u"Präsentation Administrative Tools",u"Präsentation Administrative Tools"),
    ("Analyse Parameter einer Anlagestrategie","Analyse Parameter einer Anlagestrategie"),
    ("Definition Modell","Definition Modell"),
    (u"Präsentation Modell",u"Präsentation Modell"),
    ("Analyse Kursdatenquellen","Analyse Kursdatenquellen"),
    ("Grobaufbau Schnittstellen","Grobaufbau Schnittstellen"),
    ("Analyse Output Form","Analyse Output Form"),		
    (u"Präsentation Kursdatenbank",u"Präsentation Kursdatenbank"),
    ("Analyse Backtesting Funktionalität","Analyse Backtesting Funktionalität"),
    ("Fachkonzept - administrativ","Fachkonzept - administrativ"),
    ("Fachkonzept - Review","Fachkonzept - Review"),
    ("Fachkonzept fertiggestellt","Fachkonzept fertiggestellt"),
    ("Festlegung der Anwendungsarchitektur","Festlegung der Anwendungsarchitektur"),
    ("Aufbau Teststufen","Aufbau Teststufen"),
    ("Dokumentation der Architektur","Dokumentation der Architektur"),
    (u"Präsentation Architektur / Deploymentmethoden",u"Präsentation Architektur / Deploymentmethoden"),
    ("Architektur - Review","Architektur - Review"),
    ("Architektur fertiggestellt","Architektur fertiggestellt"),
    ("Analyse technische Anforderungen an Kursdatenbank","Analyse technische Anforderungen an Kursdatenbank"),
    ("Spezifizierung generisches Anlagestrategie Modell","Spezifizierung generisches Anlagestrategie Modell"),
    ("Spezifizieurng Anlagestrategien Modul","Spezifizieurng Anlagestrategien Modul"),
    ("Spezifizierung Schnittstellen","Spezifizierung Schnittstellen"),
    ("Spezifizierung Backtesting Modul","Spezifizierung Backtesting Modul"),
    ("SRS - administrativ","SRS - administrativ"),
    ("SRS - Review","SRS - Review"),
    ("SRS fertiggestellt","SRS fertiggestellt"),
    ("Prototyping","Prototyping"),
    ("Entwicklung Datenbank","Entwicklung Datenbank"),
    ("Entwicklung Prototyp","Entwicklung Prototyp"),
  )
  name = models.CharField('Name', choices=NAME_CHOICES, max_length = 100)
  task = models.CharField('Aufgabe', choices=TASK_CHOICES, max_length = 100)

  @classmethod
  def create(cls, name, task, time, comment):
    book = cls(name=name, task=task, time=time, comment=comment, sub_date = datetime.datetime.now())
    return book

  def __unicode__(self):
    return self.name + " @ " + self.task + ": " + self.sub_date