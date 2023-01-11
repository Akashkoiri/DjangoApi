from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenRefreshView




urlpatterns = [
     # Session Token
    path('gen_auth_token/', obtain_auth_token),
    # JWT Token
    path('jwt_token/', views.MyTokenObtainPairView.as_view(), name='get_jwt_token'),
    path('jwt_token/refresh/', TokenRefreshView.as_view(), name='refresh_jwt_token'),
   
    path('register/', views.Register.as_view(), name='register'),
    path('index/', views.index, name='index'),
    path('people/', views.people, name='people'),
    path('race/', views.Race.as_view(), name='race'),
    path('all_users/', views.AllUsers.as_view(), name='all_users')
]
