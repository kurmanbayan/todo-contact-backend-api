from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse
from .models import Todo, Contact
from django.views.decorators.csrf import csrf_exempt
from django.http import QueryDict


# Create your views here.

@csrf_exempt
def todos(request):
    allTodos = Todo.objects.values()
    return JsonResponse(list(allTodos), safe=False)

@csrf_exempt
def todo_delupd(request, new_id):
    if request.method == "GET":
        todo = Todo.objects.filter(id=new_id)
        todo.delete()
        return HttpResponse("Deleted")
    elif request.method == "POST":
        data = Todo.objects.get(id=new_id)
        data.todo = request.POST["new_text"]
        print(request.POST["new_text"])
        data.save()
        return HttpResponse("Updated")
    else:
        return HttpResponse("Not defined")

@csrf_exempt

def todo_add(request):
    priority = True if request.POST["pr"] == 'true' else False
    data = Todo.objects.create(todo=request.POST["new_todo"], priority=priority)
    data.save()
    return HttpResponse("Added to db")

@csrf_exempt
def todo_done(request, new_id):
    data = Todo.objects.get(id=new_id)
    data.isDone = not data.isDone
    data.save()
    return HttpResponse("Is done updated")

@csrf_exempt
def contact(request):
    if request.method == "GET":
        allContacts = Contact.objects.values()
        return JsonResponse(list(allContacts), safe=False)

    if request.method == "POST":
        data = Contact.objects.get(id=request.POST["id"])
        data.first_name = request.POST["first_name"]
        data.last_name = request.POST["last_name"]
        data.phone_number = request.POST["phone_number"]
        data.save()

        return HttpResponse("updated")

