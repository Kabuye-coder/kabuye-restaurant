from django.forms import ModelForm

from mambo.models import Category,Dish,Customer_Table,order,payment

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields= '__all__'

class DishForm(ModelForm):
    class Meta:
        model = Dish
        fields = '__all__'

class Customer_TableForm(ModelForm):
    class Meta:
        model = Customer_Table
        fields = '__all__'

class orderForm(ModelForm):
    class Meta:
        model = order
        fields = '__all__'

class paymentForm(ModelForm):
    class Meta:
        model = payment
        fields = '__all__'

