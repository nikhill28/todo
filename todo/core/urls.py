from django.urls import path, include
from . import views

urlpatterns=[
    path("",views.home,name='home'),
    path('mark_as_done/<int:task_id>/', views.home, name='mark_as_done'),
    path('delete_task/<int:task_id>/', views.home, name='delete_task'),
    path('add/', views.add, name='add'),
]