from django.urls import path

# view 에서 만들 클래스를 갖고 온다.
from .views import *

urlpatterns = [
    path('',table,name='table'),
    path('table.html', table, name='table'),
]