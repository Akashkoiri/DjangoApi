from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerial(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create(username = validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user



class AllUserSerial(UserSerial):
    class Meta():
        model = User
        fields = ['id', 'username']


class ColorSerial(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['color_name']


class PersonSerial(serializers.ModelSerializer):
    color = ColorSerial()
    class Meta:
        model = Person
        # Which feilds we want to serialize
        # fields = ['name','age']

        ## All feilds are going to serialize
        fields = '__all__'
        ## We want to exclude some feilds
        # exclude = ['age']
        # depth = 1

        
    def validate(self, data):

        # Feild validations
        chars = ''' ~`!@#$%^&*()-+={[}]:;"'|\<,>.?/'''
        
        if  any(c in chars for c in data['name']): 
            raise serializers.ValidationError({"name": "name can't contain spaces, speacial characters"})
        
        if data['age'] < 18:
            raise serializers.ValidationError({"age": "Age should be greater than 18"})
        
        return data


best_time = 200
class DriverSerial(serializers.ModelSerializer):
    
    complete_within_time = serializers.SerializerMethodField()#'comp_in_time')

    class Meta:
        model = Driver
        fields = ['id', 'name', 'car', 'finish_time', 'complete_within_time']


    def get_complete_within_time(self, driver):
        provided_time = 60
        finish_time = getattr(driver, 'finish_time')

        if finish_time < provided_time:
            return "Yes" 
        return "No"

    