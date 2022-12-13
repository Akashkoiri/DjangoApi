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
        depth = 1

        
    def validate(self, data):

        # Feild validations
        chars = ''' ~`!@#$%^&*()-+={[}]:;"'|\<,>.?/'''
        
        if  any(c in chars for c in data['name']): 
            raise serializers.ValidationError({"name": "name can't contain spaces, speacial characters"})
        
        if data['age'] < 18:
            raise serializers.ValidationError({"age": "Age should be greater than 18"})
        
        return data

