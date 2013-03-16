from django.db import models
class Submission(models.Model):
  def __unicode__(self):
        return self.name + " @ " + self.task
        
  sub_date = models.DateTimeField('date published')
  time = models.DecimalField('time worked', max_digits=5, decimal_places=2)
  task = models.TextField('task')
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
  name = models.CharField(choices=NAME_CHOICES, max_length = 100)
# Create your models here.
