from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='computers'),
    path('details' ,views.details, name='details')
]