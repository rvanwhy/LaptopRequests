from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist

from laptopRequests.models import request


def index(req):
  """Loads the main page which contains all
  non-archived laptop requests.
  """
  entries = request.objects.filter(status__in=['Ready','Testing', 'New'])
  return render_to_response('index.html', {'requests': entries, 'archiveButton' : 'Show'})

def archived(req):
  """Loads the main page including archived
  requests.
  """
  entries = request.objects.all()
  return render_to_response('index.html', {'requests': entries, 'archiveButton':'Hide'})

def getDetails(req, requestNumber):
  """Attempts to grab a request's details and
  display them for the user. If no requst is found,
  it simply displays 'Request not found!'
  """
  try:
    entry = request.objects.get(id=requestNumber)
  except ObjectDoesNotExist:
    return HttpResponse('<h1>Request not found!</h1><p>Are you sure your url is correct?</p>')

  return render_to_response('request.html', {'request': entry})
