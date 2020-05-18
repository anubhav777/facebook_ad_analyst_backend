from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from .models import Usersearchhistory

class Userserializer(serializers.ModelSerializer):
    email=serializers.EmailField(required=True,validators=[UniqueValidator(queryset=User.objects.all())])
    username=serializers.CharField(required=True,validators=[UniqueValidator(queryset=User.objects.all())])
    password=serializers.CharField(min_length=8)

    def create(self,validated_data):
        user= User.objects.create_user(validated_data['email'],validated_data['username'],validated_data['password'])
        return user
    
    class Meta:
        model=User
        fields=('id','username','email','password')
        extra_kwargs={
            'password':{'write_only':True}
        }
class UserSearchdisp(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Usersearchhistory
        fields=('id','searchquery','userid','date')

