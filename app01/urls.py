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
        path('updateonemore/',updateonemore),
        path('manytomanyadd/',manytomanyadd),
        path('manytomanyget/',manytomanyget),
        path('manytomanyupdate/',manytomanyupdate),
        path('manytomanydelete/',manytomanydelete),
        path('juhequery/',juhequery),
        path('Ftest/',Ftest),
        path('Qtest/',Qtest),
        ]