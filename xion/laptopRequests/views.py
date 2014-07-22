from django.shortcuts import render_to_response

from laptopRequests.models import request

def index(req):
  entries = request.objects.all().filter(status__in=['Ready','Testing', 'New'])
  return render_to_response('index.html', {'requests': entries, 'archiveButton' : 'Show'})

def archived(req):
  entries = request.objects.all()
  return render_to_response('index.html', {'requests': entries, 'archiveButton':'Hide'})

def getDetails(req, requestNumber):
  entries = request.objects.all().filter(id=requestNumber)
  return render_to_response('request.html', {'requests': entries})
