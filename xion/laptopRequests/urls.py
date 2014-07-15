from django.conf.urls import url

from laptopRequests import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]