from django.contrib import admin
from users.models import Role
from crm.models import *


admin.site.register(Tables)
admin.site.register(Role)
admin.site(Departments)
admin.site(Meal_Categories)
admin.site(Statuses)
admin.site(Meals)
admin.site(ServicePercentage)
admin.site(Orders)
admin.site(MealsToOrders)
admin.site(Checks)