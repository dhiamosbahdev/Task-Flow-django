from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('task/<int:pk>/update/', views.update_task, name='update_task'),
    path('task/<int:pk>/delete/', views.delete_task, name='delete_task'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path ('ajax/',views.task_list_ajax,name='task_list_ajax'),
    path('toggle/<int:pk>/', views.toggle_task, name='toggle_task'),
]