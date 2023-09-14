from rest_framework import generics, status
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer

class PersonCreateView(generics.CreateAPIView):  # Use CreateAPIView for POST requests
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonRetriveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


'''from .models import Person
from rest_framework import generics
from .serializers import PersonSerializer


# Create your views here.

class PersonCreateView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
class PersonRetriveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer'''
