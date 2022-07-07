from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Student
from api.serializers import StudentSerializer

def home(request):
    return HttpResponse("<h1>Hello World</h1>")

def stu_obj(request,id):
    stu_obj = Student.objects.get(id=id)
    serializer = StudentSerializer(stu_obj)
    return JsonResponse(serializer.data)

def stu_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu,many = True)
    return JsonResponse(serializer.data,safe=False)
