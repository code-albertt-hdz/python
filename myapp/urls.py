from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('hello/<str:user>',views.hello),
    path('about/',views.about),
    path('projects/',views.projects),
    path('tasks/',views.tasks),
    path('task_detail/<int:id>/',views.task_detail),
    path('create_task/',views.create_task),
    path('create_project/',views.create_project)
]