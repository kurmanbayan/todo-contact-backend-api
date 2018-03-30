from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.todos),
    path('todos/<int:new_id>/', views.todo_delupd),
    path('todos/<int:new_id>/done/', views.todo_done),
    path('todos/add/', views.todo_add),


]
