# from rest_framework import viewsets
# from .serializers import UserSerializer,AdminSerializer
from django.contrib.auth.models import User
from django.contrib.auth import login
# from rest_framework.authentication import  BasicAuthentication
# from rest_framework.permissions import IsAuthenticated

# # # Create your views here.




from rest_framework.views import APIView

class MyAPI(APIView):
   def get(self, request, *args, **kwargs):
      users = User.objects.all()
      data = UserSerializer(users,many=True).data
      return Response({"data":data})

   def post(self, request, *args, **kwargs):
      username = request.data.get("username")
      password = request.data.get("password")
      # data = request.data
      user = User.objects.create(username=username, password= password)
      login(request,user)
      return Response({"msg":"logged in"})

'''
{
"username": "mukhtar",
"password": "admin"
}
'''


class LoginAPI(APIView):
   def post(self, request, *args, **kwargs):
      username = request.data.get("username")
      password = request.data.get("password")
      data = request.data
      user = User.objects.create(username=username, password= password)
      login(request,user)
      return Response({"msg":"logged in"})



class RegisterAPI(APIView):
   def post(self, request, *args, **kwargs):
      username = request.data.get("username")
      password = request.data.get("password")
      data = request.data
      user = User.objects.create(username=username, password= password)
      login(request,user)
      return Response({"msg":"logged in"})