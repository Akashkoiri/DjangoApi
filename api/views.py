from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Person, Driver
from .serializers import *
from django.contrib.auth.models import User
# Token Authentication 
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
# JWT Token
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
# For setting permissions 
from rest_framework.permissions import IsAuthenticated



# Only allow GET & POST Method
@api_view(['GET', 'POST'])
def index(request):
    courses = {
        'name': 'Python',
        'items': ['Django','Flask','FastApi','Tornado'],
        'provider': 'Scaler'
    }

    if request.method == 'GET':
        return Response(courses)

    elif request.method == 'POST':
        data = request.data
        return Response(data)


@api_view(['GET','POST','PUT','PATCH'])
def people(request):        
    if request.method == 'GET':
        lst = []
        
        def get_item(item):
            if 'id' in item:
                try:
                    people = Person.objects.get(id = item['id'])
                    serialized = PersonSerial(people)
                    return serialized.data
                except:
                    return {"id": f"id {item['id']} dosen't exist"}
            return {"Error": "please provide an id"}

        if request.data:
            print("yes")
            if type(request.data) == list:
                for item in request.data:
                    lst.append(get_item(item))
                return Response(lst)

            else:
                return Response(get_item(request.data))


        people = Person.objects.all()
        serialized = PersonSerial(people, many=True)
        return Response(serialized.data)



    if request.method == 'POST':
        print(request.data)
        serialized = PersonSerial(data = request.data)
        if serialized.is_valid():
            serialized.save()
            return Response('Object created')
        return Response(serialized.errors)


# Here we are only updating data
  
    if request.method == 'PUT':
        people = Person.objects.get(id=request.data['id'])
        serialized = PersonSerial(people, data = request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data)
        return Response(serialized.errors)

    if request.method == 'PATCH':
        people = Person.objects.get(id=request.data['id'])
        serialized = PersonSerial(people, data = request.data, partial=True)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data)
        return Response(serialized.errors)
 

# Here we are only deleting data
  
    if request.method == 'DELETE':
        people = Person.objects.get(id=request.data['id'])
        people.delete()
        return Response({'message': 'Person deleted'})


# Class based api
class Race(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        drivers = Driver.objects.all()
        serialized = DriverSerial(drivers, many=True)
        return Response({"user": str(request.user), "data" : serialized.data})


class AllUsers(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):

        print(request.user)

        users = User.objects.all()
        serialized = AllUserSerial(users, many=True)
        return Response(serialized.data)


## This Register api use Simple Token to restrict
# class Register(APIView):
#     def post(self, request):
#         serialized = UserSerial(data = request.data)

#         if not serialized.is_valid():
#             return Response(serialized.errors)

#         serialized.save()
        
#         user = User.objects.get(username = serialized.data['username'])
        # token = Token.objects.create(user = user)


#         return Response({
#             "massage": "User created", 
#             "data": serialized.data,
#             "token": token.key
#         })


## This api uses JWT Token to restrict
class Register(APIView):
    def post(self, request):
        serialized = UserSerial(data = request.data)

        if not serialized.is_valid():
            return Response(serialized.errors)

        serialized.save()
        
        user = User.objects.get(username = serialized.data['username'])
        ref_token = RefreshToken.for_user(user)


        return Response({
            "massage": "User created", 
            "data": serialized.data,
            "JWT_token": {
                "access": str(ref_token.access_token),
                "refresh": str(ref_token)
            }
        })


# We are overwrighting sum classes to encrypt some other data to JWT token
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Whatever datafield you want to add
        token['username'] = user.username
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

