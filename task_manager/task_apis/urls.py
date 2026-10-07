from django.urls import path
from task_apis.views import TaskListView, TaskDetailView, TaskEditView, TaskDeleteView, AddTaskView

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('task/<int:pk>/edit/', TaskEditView.as_view(), name='task-edit'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('task/add/', AddTaskView.as_view(), name='add-task'),
]