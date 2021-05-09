from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
# Create your views here.


def register(request):
    print(request.method)
    # print(dir(request))
    if request.method == "GET":
        employee = Employee.objects.all()
        print(employee.query)
        print(" i am in views register function")
        # print("request data is ", request.data)
        # print("request headers ", request.headers)
        # print("request Meta ", request.Meta)
        return render(request,'hello.html', {"employee": employee})