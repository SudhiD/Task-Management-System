from django.shortcuts import render
from rest_framework.views import APIView
from task_apis.models import TasksModel
from task_apis.serializers import TasksSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

# Create your views here.



class AddTaskView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer = TasksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        tasks = TasksModel.objects.all()
        serializer = TasksSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TaskDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,pk):
        task = TasksModel.objects.get(id=pk)
        serializer = TasksSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)    

class TaskEditView(APIView):
    permission_classes = [IsAuthenticated]
    def put(self,request,pk):
        task = TasksModel.objects.get(id=pk)
        serializer = TasksSerializer(task,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskSearchView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        search = request.GET.get("search", "")

        tasks = TasksModel.objects.filter(
            title__icontains=search
        )

        serializer = TasksSerializer(tasks, many=True)

        return Response(serializer.data)    

class TaskDeleteView(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self,request,pk):
        task = TasksModel.objects.get(id=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    

    
