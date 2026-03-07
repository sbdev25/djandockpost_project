from django.urls import path 
from . import views 

urlpatterns = [
    
    path('' , views.getUsers) , 
    path('read/<str:pk>/' , views.getUser_pk),
    path('create/' , views.addUser),
    path('update/<str:pk>/' , views.updateUser),
    path('delete/<str:pk>/' , views.deleteUser),
    
]
