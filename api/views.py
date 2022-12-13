from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerial


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


