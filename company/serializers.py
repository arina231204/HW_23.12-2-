from rest_framework import serializers

from .models import Positions,Employees

class PositionsSerializer(serializers.Serializer):
    positions = serializers.CharField(max_length=225)
    department = serializers.CharField(max_length=225)


    def create(self, validated_data):
        positions = Positions.objects.create(
            positions = validated_data['positions'],
            department = validated_data['department'],
        )
        return positions

    def update(self, instance,validated_data):
        instance.positions = validated_data['positions']
        instance.department = validated_data['department']
        return instance

class EmployeesSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=225)
    birth_date = serializers.DateTimeField()
    positions = serializers.CharField(max_length=225)
    salary = serializers.IntegerField()


    def create(self, validated_data):
        employees = Employees.objects.create(
            name = validated_data['name'],
            birth_date = validated_data['birth_date'],
            positions = validated_data['positions'],
            salary = validated_data['salary'],
        )
        return employees

    def update(self, instance,validated_data):
        instance.name = validated_data['name'],
        instance.birth_date = validated_data['birth_date'],
        instance.positions = validated_data['positions'],
        instance.salary = validated_data['salary'],
        return instance