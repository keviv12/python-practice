# from rest_framework import serializers

# from django.contrib.auth.models import User

# class UserSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = User
#        fields = ('__all__')



# class AdminSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = User
#        fields = ('id','username','first_name')




from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Student,TopPeople





class UserSerializer(serializers.ModelSerializer):
   class Meta:
       model = User
       fields = ('__all__')
    



class StudentSerializer(serializers.Serializer):
    class Meta:
       model = Student
       fields = ('__all__')
    


    def create(self, validated_data):
    
        return Student.objects.create(**validated_data)


class TopPeopleSerializer(serializers.Serializer):
    name=serializers.CharField(required=False, allow_blank=True, max_length=100)
    country=serializers.CharField(required=False, allow_blank=True, max_length=100)
    age=serializers.CharField(required=False, allow_blank=True, max_length=100)
    mobile=serializers.CharField(required=False, allow_blank=True, max_length=100)

