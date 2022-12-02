from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerial


# Only allow GET & POST Method
@api_view(['GET', 'POST'])       #We can also add more
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


@api_view(['GET','POST'])
def people(request):
    if request.method == 'GET':
        peoples = Person.objects.all()
        serialized = PersonSerial(peoples, many=True)
        return Response(serialized.data)
    
    if request.method == 'POST':
        serialized = PersonSerial(data = request.data)
        if serialized.is_valid():
            serialized.save()
            return Response('Object created')
        return Response(serialized.errors)
 
