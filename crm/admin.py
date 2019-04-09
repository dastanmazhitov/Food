from django.contrib import admin
from users.models import Role
from crm.models import *

admin.site.register(Tables)
admin.site.register(Role)
admin.site.register(Departments)
admin.site.register(Meal_Categories)
admin.site.register(Statuses)
admin.site.register(Meals)
admin.site.register(ServicePercentage)
admin.site.register(Orders)
admin.site.register(MealsToOrders)
admin.site.register(Checks)
