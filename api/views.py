from rest_framework.decorators import api_view
from rest_framework.response import Response




@api_view(['GET'])
def index(request):
    courses = {
        'name':'Python',
        'items':['Django','Flask','FastApi','Tornado'],
        'provider':'Scaler'
    }
    return Response(courses)

