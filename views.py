
from django.contrib.auth.models import User
from django.http import response
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate , login ,logout

# Create your views here.

class UserAPI(APIView):
    def get(self,request,*args,**kwargs):
        user=User.objects.all()
        data=UserSerializer(user,many=True).data
        return Response({"data":data})



class RegisterAPI(APIView):
    def post(self,request,*args,**kwargs):
        username= request.data.get('username')
        password= request.data.get('password')
        if User.objects.filter(username=username).exists():
            return Response({"msg":"username already exist"})
        user=User.objects.create(username=username,password=password)

        return Response({"msg":"user created"})



class LoginAPI(APIView):
    def post(self,request,*args,**kwargs):
        username= request.data.get('username')
        password= request.data.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return Response({"msg":"logged in success"})
        return Response({"msg":"Invalid details !"})
    

    def patch(self,request,*args,**kwargs):
        if User.objects.filter(username=request.data.get('username')).exists():
            user=User.objects.get(username=request.data.get("username"))
            serializer=UserSerializer(request.data,many=True)
            print(serializer)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg":"profile updated success "})
            return Response({"msg":"Invalid details !"})
        return Response({"msg":"User not found !"})





class deleteAPI(APIView):
    def post(self,request,*args,**kwargs):
        username= request.data.get('username')
        password= request.data.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            user.delete()
            return Response({"msg":"user deleted Success"})
        return Response({"msg":"Invalid details !"})




