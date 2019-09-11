from django.urls import path
from .views import *

urlpatterns = [
        path('index/',index),
        path('addperson/',addperson),
        path('getperson/',getperson),
        path('updateperson/',updateperson),
        path('deleteperson/',deleteperson),
        path('addOneMore/',addOneMore),
        path('getOneMore/',getOneMore),
        ]