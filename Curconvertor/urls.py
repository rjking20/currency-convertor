
from django.urls import path
from .views import home,convertor,buttonAction
urlpatterns = [
  
    path('',convertor,name='currency'),
    path('Action/',buttonAction,name='buttonAction'),
]
