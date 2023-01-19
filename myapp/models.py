from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    done = models.BooleanField(default=False)
    #Llave foranea, para eliminar los datos en cascada
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.title + ' => ' + self.project.name
