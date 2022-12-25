from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.utils import json

from company.models import Positions, Employees
from company.serializers import PositionsSerializer, EmployeesSerializer


# class PositionsViewSet(viewsets.ModelViewSet):
#     queryset = Positions.objects.all()
#     serializer_class = PositionsSerializer
#
# class EmployeesViewSet(viewsets.ModelViewSet):
#         queryset = Employees.objects.all()
#         serializer_class = EmployeesSerializer

@csrf_exempt
def create_Positions(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_comment = Positions.objects.create(**data)
        json_data = {
            "positions": new_comment.positions,
            "department": new_comment.department,
        }
        print(new_comment)
        return HttpResponse("OK")
    if request.method == 'GET':
        comments = Positions.objects.all()
        data = []
        for comment in comments:
            data.append(
                {
                    'positions': comment.positions,
                    'department': comment.department,
                }
            )
        json_data = json.dumps(data)
        return JsonResponse(json_data, safe=False)


@csrf_exempt
def create_employees(request):
    if request.method == "POST":
        data = json.loads(request.body)
        new_mark = Employees.objects.create(**data)
        json_data = {
            "name": new_mark.name,
            "birth_date": new_mark.birth_date,
            "positions": new_mark.positions,
            "salary": new_mark.salary,
        }
        print(new_mark)
        return HttpResponse("OK")
    if request.method == 'GET':
        marks = Employees.objects.all()
        data = []
        for mark in marks:
            data.append(
                {
                    "name": mark.name,
                    "birth_date": mark.birth_date,
                    "positions": mark.positions,
                    "salary": mark.salary,
                }
            )
        json_data = json.dumps(data)
        return JsonResponse(json_data, safe=False)