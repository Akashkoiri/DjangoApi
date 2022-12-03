from django.urls import path
from . import views




urlpatterns = [
    path('index/', views.index, name='index'),
    path('people/', views.people, name='people'),
    # I've created this for explaining PUT & PATCH methods
    path('people1/', views.people1, name='people1'),
]
