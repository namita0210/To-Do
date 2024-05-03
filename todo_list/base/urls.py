from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('' , TaskList.as_view(), name="tasks" ) ,
    path('task/<int:pk>' , TaskDetail.as_view(), name="task" ) 


]