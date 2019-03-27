from django.db import models
from users.models import *
from rest_framework import generics


class Tables(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Roles(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Departments(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Meal_Categories(models.Model):
    name = models.CharField(max_length=50)
    departmentsid = models.ForeignKey(Departments, on_delete=models.CASCADE, null=True)


class Statuses(models.Model):
    name = models.CharField(max_length=100, default='in progress')

    def __str__(self):
        return self.name


class Meals(models.Model):
    name = models.CharField(max_length=50)
    categoryid = models.ForeignKey(Meal_Categories, on_delete=models.CASCADE, null=True)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class ServicePercentage(models.Model):
    name = models.IntegerField(default=15)


class Orders(models.Model):
    waiterid = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    tablesid = models.ForeignKey(Tables, on_delete=models.CASCADE, null=True)
    statusid = models.ForeignKey(Statuses, on_delete=models.CASCADE, null=True)
    mealsid = models.ForeignKey(Meals, on_delete=models.CASCADE, null=True)
    tablesname = models.CharField(max_length=100)
    date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.tablesname


class MealsToOrders(models.Model):
    count = models.IntegerField(default=1)
    orderid = models.ForeignKey(Orders, on_delete=models.CASCADE, null=True)
    mealsid = models.ForeignKey(Meals, on_delete=models.CASCADE, null=True)


class Checks(models.Model):
    orderid=models.ForeignKey(Orders, on_delete=models.CASCADE, null=True)
    percentage = models.ForeignKey(ServicePercentage, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(blank=True, null=True)
    mealsid = models.ForeignKey(Meals, on_delete=models.CASCADE, null=True)
    totalsum = models.CharField(max_length=100)
