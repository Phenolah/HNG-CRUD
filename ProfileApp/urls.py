from django.urls import path
from .views import *

urlpatterns =[
    path('api/', PersonView.as_view(), name=''),
    #path('api/<int:pk>', PersonRetriveUpdateDeleteView.as_view(), name='')
]