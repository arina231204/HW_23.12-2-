from django.db import models

class Positions(models.Model):
    positions = models.CharField(max_length=225)
    department = models.CharField(max_length=225)

    def __str__(self):
        return f'{self.positions} - {self.department}'


class Employees(models.Model):
    name = models.CharField(max_length=225)
    birth_date = models.DateTimeField()
    positions = models.CharField(max_length=225)
    salary = models.IntegerField()

    def __str__(self):
        return self.name





