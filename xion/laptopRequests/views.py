from django.shortcuts import render_to_response

from laptopRequests.models import request

def index(req):
  entries = request.objects.all()
  color = {'New': 'gray', 'Started': 'blue', 'Testing': 'orange', 'Ready':'green', 'Archive': 'pink'}
  return render_to_response('index.html', {'requests': entries, 'color': color, 'admin': 0})
