from django.urls import path, include
from . import views

urlpatterns=[
    path("",views.home,name='home'),
    path('add/', views.add, name='add'),
    path('done/<int:pk>/', views.done, name='done'),
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),
] 