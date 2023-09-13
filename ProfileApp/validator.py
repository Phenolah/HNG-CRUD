from .models import Person
from rest_framework import serializers

def validate_name(value):
    query_set = Person.objects.filter(name__iexact=value)
    if query_set.exists():
        raise serializers.ValidationError(f"The name {value} already exists")