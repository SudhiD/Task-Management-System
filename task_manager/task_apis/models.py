from django.db import models

# Create your models here.

class TasksModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=[("Todo", "Todo"), ("In Progress", "In Progress"), ("Completed", "Completed")])
    priority = models.CharField(max_length=20, choices=[("Low", "Low"), ("Medium", "Medium"), ("High", "High")])
    due_date = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)

