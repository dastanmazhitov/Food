from crm.models import *
from crm.serializers import *
from rest_framework import generics


class TablesViewSet(generics.ListCreateAPIView):
    queryset = Tables.objects.all()
    serializer_class = TablesSerializer


class TablesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tables.objects.all()
    serializer_class = TablesSerializer


class RolesViewSet(generics.ListCreateAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer


class RolesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer


class DepartmentsViewSet(generics.ListCreateAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer


class DepartmentsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer


class MealsCategoriesViewSet(generics.ListCreateAPIView):
    queryset = Meal_Categories.objects.all()
    serializer_class = Meals_CategoriesSerializer


class MealsCategoriesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meal_Categories.objects.all()
    serializer_class = Meals_CategoriesSerializer


class StatusesViewSet(generics.ListCreateAPIView):
    queryset = Statuses.objects.all()
    serializer_class = StatusesSerializer


class StatusesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Statuses.objects.all()
    serializer_class = StatusesSerializer


class MealsViewSet(generics.ListCreateAPIView):
    queryset = Meals.objects.all()
    serializer_class = MealsSerializer


class MealsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meals.objects.all()
    serializer_class = MealsSerializer


class ServicePercentageViewSet(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer


class ServicePercentageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServicePercentage.objects.all()
    serializer_class = ServicePercentageSerializer


class OrdersViewSet(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer


class OrdersDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
#@@@@@@


class MealsToOrdersViewSet(generics.ListCreateAPIView):
    queryset = MealsToOrders.objects.all()
    serializer_class = MealsToOrdersSerializer


class MealsToOrdersDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MealsToOrders.objects.all()
    serializer_class = MealsToOrdersSerializer
    #queryset = Meal_Categories.objects.all()
    #serializer_class = Meals_CategoriesSerializer


class ChecksViewSet(generics.ListCreateAPIView):
    queryset = Checks.objects.all()
    serializer_class = ChecksSerializer


class ChecksDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Checks.objects.all()
    serializer_class = ChecksSerializer
