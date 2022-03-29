from django.conf.urls import url 
from . import views

urlpatterns =[
    url(r'^getRecordsAPI/(?P<date>\d{4}-\d{2}-\d{2})$',views.getRecordsAPI),
]