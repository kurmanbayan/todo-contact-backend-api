from django.db import models

# Create your models here.

class Todo(models.Model):
    todo = models.CharField(max_length=500)
    isDone = models.BooleanField(default=False)
    priority = models.BooleanField(default=True)

    def __str__(self):
        return self.todo

class Contact(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=300)
    img = models.CharField(max_length=500, default='')