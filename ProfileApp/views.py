
from .models import Person
from rest_framework import generics
from .serializers import PersonSerializer


# Create your views here.

class PersonCreateView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
class PersonRetriveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
