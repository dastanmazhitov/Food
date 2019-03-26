from rest_framework import serializers
from .models import *


class TablesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tables
        fields = ('id', 'name',)


class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = ('id', 'name',)


class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('id', 'name',)


class Meals_CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal_Categories
        fields = ('id', 'name', 'departmentsid',)


class StatusesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statuses
        fields = ('id', 'name',)


class MealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statuses
        fields = ('id', 'name',)
