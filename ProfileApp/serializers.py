from rest_framework import serializers
from .models import Person
from . import validator

class PersonSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[validator.validate_name])
    class Meta:
        model = Person
        fields = "__all__"