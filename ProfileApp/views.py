from django.shortcuts import render
from .models import Person
from rest_framework import generics
from .serializers import PersonSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class PersonView(generics.GenericAPIView):

    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_field = 'pk'

    def post(self,request):
        serializer = PersonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)





'''class PersonCreateView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
class PersonRetriveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer'''
