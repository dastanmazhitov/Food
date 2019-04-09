from rest_framework import serializers
from crm.models import *


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


class ServicePercentageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicePercentage
        fields = ('id', 'name',)


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('id', 'waiterid', 'tablesid', 'statusid', 'mealsid', 'tablesname', 'date',)


class MealsToOrdersSerializer(serializers.ModelSerializer):
    class Meta: 
        model = MealsToOrders
        fields = ('id', 'count', 'orderid', 'mealsid',)


class ChecksSerializer(serializers.ModelSerializer):
    totalsum = serializers.SerializerMethodField()

    def get_totalsum(self, request):
        sum = 0
        mto = MealsToOrders.objects.filter(orderid=request.orderid)
        for s in mto:
            sum += s.count * s.mealsid.price
        return sum

    class Meta:
        model = Checks
        fields = ('id', 'orderid', 'percentage', 'date', 'mealsid', 'totalsum',)
