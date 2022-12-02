from rest_framework import serializers
from .models import Person

class PersonSerial(serializers.ModelSerializer):
    class Meta:
        model = Person
        # Which feilds we want to serialize
        # fields = ['name','age']

        ## All feilds are going to serialize
        fields = '__all__'
        ## We want to exclude some feilds
        # exclude = ['age']
