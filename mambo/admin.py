from django.contrib import admin

from .models import Category, Dish, Customer_Table, order,payment

class CategoryAdmin(admin.ModelAdmin):
    list_display= ("name_of_category","no_of_category","date_of_categorysale","address","category_type","description")




admin.site.register(Category, CategoryAdmin)

class DishAdmin(admin.ModelAdmin):
    list_display= ("dish_details","price","category")

admin.site.register(Dish, DishAdmin)

class Customer_TableAdmin(admin.ModelAdmin):
    list_display= ("table_type","status")

admin.site.register(Customer_Table, Customer_TableAdmin)


class orderAdmin(admin.ModelAdmin):
    list_display= ("order_date","dish","quantity","table","served_by")

admin.site.register(order, orderAdmin)

class paymentAdmin(admin.ModelAdmin):
    list_display = ("order","amount","received_by")

admin.site.register(payment, paymentAdmin)











