# -*- coding: utf-8 -*-
# Create your views here.
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Reset
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.db import models
from django.forms import ModelForm
from django.db.models import Sum
import django_tables2 as tables
from django_tables2 import RequestConfig
from models import *
import datetime

class SubmissionForm(ModelForm):
  class Meta:
  	model = Submission
  	exclude = ('sub_date',)
  	
  def __init__(self, *args, **kwargs):
  	super(SubmissionForm, self).__init__(*args, **kwargs)
  	self.helper = FormHelper(self)
   	self.helper.form_method = 'POST'
   	self.helper.form_class = 'form-horizontal'
   	self.helper.layout = Layout(
   		Field('name'),
   		AppendedText('time', 'h', placeholder='1.5',),
   		Field('task'),
   		Field('comment', placeholder='Anpassen der fachlichen Analyse.'),
   		FormActions(
       Submit('save_changes', 'Melden', css_class="btn-primary"),
       Reset('cancel', 'Reset'),
       )
     )
  	
  	
def submit_me(request):
  if request.method == 'POST':
    form = SubmissionForm(request.POST)
    if form.is_valid():
      f = SubmissionForm(request.POST)
      submission = f.save(commit=False)
      submission.sub_date = datetime.datetime.now()
      submission.save()
#       from django.core.mail import send_mail
#       send_mail(subject, message, sender, recipients)
      return HttpResponseRedirect('http://j12d.de/timetracker/times/')
  else:
    form = SubmissionForm()
  return render_to_response('submit_me.html', RequestContext(request,  {'form': form, }))

class NameForm(forms.Form):
	NAME_CHOICES = (
	("1","Alle"),
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
	name = forms.ChoiceField(NAME_CHOICES)
	
  
class SubmissionTable(tables.Table):
	class Meta:
		model = Submission
		attrs = {"class": "paleblue"}

def table(request):
  if request.method == 'POST':
  	form = NameForm(request.POST)
  	if form.is_valid():
  		name = form.cleaned_data['name']
  		if name == '1':
  			query_results = Submission.objects.all().order_by('-sub_date')
  			cum_hours = Submission.objects.filter(name=name).aggregate(Sum('time'))
  			cum_hours = cum_hours['time__sum']
  		else:
  			try:
  				query_results = Submission.objects.filter(name=name).order_by('-sub_date')
  				cum_hours = Submission.objects.filter(name=name).aggregate(Sum('time'))
  				cum_hours = cum_hours['time__sum']
  			except Submission.DoesNotExist:
  				query_results = Submission.objects.none()
  				cum_hours = 0
  		table = SubmissionTable(query_results)
  		RequestConfig(request, paginate={"per_page": 20}).configure(table)
  		return render_to_response('times.html', RequestContext(request, {
		  	'times': query_results,
		  	'form': form,
		  	'table': table,
		  	'timesum': cum_hours,
		  	})
		  )
  else:
  	form = NameForm()
  	query_results = Submission.objects.all().order_by('-sub_date')
  	table = SubmissionTable(query_results)
  	RequestConfig(request, paginate={"per_page": 20}).configure(table)
  return render_to_response('times.html', RequestContext(request, {
  	'times': query_results,
  	'form': form,
  	'table': table,
  	})
  )
  

class ReportTable(tables.Table):
	sumtime = tables.Column(verbose_name="Arbeitszeit")
	class Meta:
		model = Submission
		fields = ('name', 'sumtime')
		attrs = {"class": "paleblue"}
  
def report(request):
  if request.method == 'POST':
    query_results = Submission.values('name').order_by('name').annotate(sumtime=Sum('time'))

  else:
    query_results = Submission.objects.values("name").annotate(sumtime=Sum('time')).order_by('-sumtime')
    table = ReportTable(query_results)
    RequestConfig(request).configure(table)
  return render_to_response('report.html', RequestContext(request, {
  	'table': query_results,
  	'times': table,
  	})
  )