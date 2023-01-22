from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject

# Create your views here.
def index(request):
    title = "to django course"
    return render(request,"index.html", {
        "title" : title
    })

def projects(request):
    #project = list(Project.objects.values())
    projects = Project.objects.all()#Obtener todos los objetos
    return render(request,"projects/projects.html",{
        "projects":projects
    })
    #return JsonResponse(project, safe=False) #Retornar en objeto de JSON

def tasks(request):
    #task = Task.objects.get(id=id)
    #Para devolver un 404 en caso de no devolver datos
    #task = get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request,"tasks/tasks.html",{
        "tasks":tasks
    })
    #return HttpResponse('<h1>Task: </h1> %s '% task.title)

def create_task(request):   
    if request.method == 'GET':
        return render(request,"tasks/create_task.html",{
             "form" : CreateNewTask()
        })
    else:
        Task.objects.create(title=request.POST['title'], description=request.POST['description'],
        project_id=1)
        return redirect("/tasks/")

def create_project(request):
    if request.method == 'GET':
        return render(request, "projects/create_project.html",{
            "form" : CreateNewProject() 
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect("/projects/")

def task_detail(request,id):
    task = Task.objects.filter(project_id=id)
    project = Project.objects.get(id=id)
    return render(request,"tasks/task_detail.html",{
        "project" : project,
        "tasks":task
    })
