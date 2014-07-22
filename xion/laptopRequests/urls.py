from django.conf.urls import url

from laptopRequests import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^archived$', views.archived, name='archived'),
    url(r'^([0-9]*)$', views.getDetails, name='getDetails')
]
