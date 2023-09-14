from django.urls import path
from .views import *

urlpatterns =[
    path('api', PersonCreateView.as_view()),
    path('api/<int:pk>', PersonRetriveUpdateDeleteView.as_view())
]