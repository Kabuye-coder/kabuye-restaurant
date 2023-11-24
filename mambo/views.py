from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required
from django.contrib import messages


from mambo.forms import CategoryForm,DishForm,Customer_TableForm,orderForm,paymentForm
from mambo.models import Category,Dish,Customer_Table,order,payment #This helps us to access the category model when initiating Category.Objects()


@login_required
def index_view(request):
    return render(request, 'index.html')

def home_view(request):
    return render(request, 'home.html')

def contact_view(request):
    return render(request, 'contact.html')

def foodyard_view(request):
    return render(request, 'foodyard.html')


@login_required
def add_category_view(request):
    message = ''
    if request.method == "POST":
        category_form = CategoryForm(request.POST)


        if category_form.is_valid():
            category_form.save()

            messages.success (request,"category added successfuly")


    
   #here for this we put a GET method that handles the else part
    category_form = CategoryForm()

    category = Category.objects.all()

    context = {
        'form':category_form,
        'msg':message,
        'category':category
    }

    return render(request, "add_category.html",context)

@login_required
def edit_category_view(request, category_id): #category is a variable that stores the details as shown
    message = ''
    category = Category.objects.get(id= category_id)
    #here we specify the method for the url as seen
    if request.method == "POST":
        category_form = CategoryForm(request.POST, instance=category)

        #then we check whether the form has valid data as seen
        if category_form.is_valid():#then we go ahead and save the form
            category_form.save() #this is the save method after the validation as seen

            messages.success (request,"Edited successfuly")

        else:
            message="its invalid"

    else:#remember that if the method is a POST then the else is the defaullt as seen
        category_form = CategoryForm(instance=category)
        #this will contain the current existing data displaying it in the form

    context = {
        'form':category_form,
        'category':category
    }
    return render(request, 'edit_category.html', context)

def delete_category_view(request, category_id):
    category = Category.objects.get(id= category_id)

    category.delete()

    return redirect(add_category_view)

@login_required
def add_dish_view(request):
    message = ''
    if request.method == "POST":
        dish_form = DishForm(request.POST,request.FILES)

        if dish_form.is_valid():
            dish_form.save()

            messages.success(request,"dish added successfuly")
     
    
   
    dish_form = DishForm()

    dishes = Dish.objects.all()

    context ={
    'form':dish_form,
    'msg': message,
    'dishes': dishes
}


    return render(request, "add_dish.html",context)
    

@login_required
def edit_dish_view(request, dish_id): #category is a variable that stores the details as shown
        message = ''
        dish = Dish.objects.get(id= dish_id)
        #here we specify the method for the url as seen
        if request.method == "POST":
            dish_form = DishForm(request.POST,request.FILES, instance=dish)

            #then we check whether the form has valid data as seen
            if dish_form.is_valid():#then we go ahead and save the form
                dish_form.save() #this is the save method after the validation as seen

                message = "Changes saved successfuly"
                return redirect(add_dish_view)

            else:
                message = "Invalid data"

        else:#remember that if the method is a POST then the else is the defaullt as seen
            dish_form = DishForm(instance=dish)
            #this will contain the current existing data displaying it in the form
        dishes = Dish.objects.all() 
        context = {
            'form':dish_form,
            'dish':dish,
            #'category':dish
            'msg':message
        }
        return render(request, 'edit_dish.html', context)


@login_required
def delete_dish_view(request, dish_id):
    dish = Dish.objects.get(id = dish_id)

    dish.delete()

    return redirect(add_dish_view)

    



@login_required
def add_customer_view(request):
    message = ''
    if request.method == "POST":
        customer_form = Customer_TableForm(request.POST)

        if customer_form.is_valid():
            customer_form.save()
            messages.success (request,"customer added successfuly")




   
    customer_form = Customer_TableForm()

    

    customer = Customer_Table.objects.all()

    context = {
        'form':customer_form,
        'msg':message,
        'customer':customer,
    }

    return render(request,"add_customer.html",context)


@login_required
def edit_customer_table_view(request, customer_id):
    message = ''

    customer = Customer_Table.objects.get(id= customer_id)

    if request.method == "POST":
        customer_form = Customer_TableForm(request.POST, instance=customer)

        if customer_form.is_valid():#then we go ahead and save the form
            customer_form.save() #this is the save method after the validation as seen

            message = "Changes saved successfuly"

        else:
            message = "Invalid data"

    else:#remember that if the method is a POST then the else is the defaullt as seen
        customer_form = Customer_TableForm(instance=customer)

    context = {
        'form':customer_form,
        'customer':customer
    }
    return render(request, 'edit_customer.html', context)

@login_required
def delete_customer_table_view(request, customer_id):
    customer = Customer_Table.objects.get(id= customer_id)

    customer.delete()

    return redirect(add_customer_view)

@login_required
def add_order_view(request):
    message = ''
    if request.method == "POST":
        order_form = orderForm(request.POST)

        if order_form.is_valid():
            order_form.save()
            
            messages.success (request,"order added successfuly")

    


        
   
    order_form = orderForm()
    

    plates = order.objects.all()

    context = {
        'form':order_form,
        'msg':message,
        'plates':plates

    }

    return render(request,"add_order.html",context)

@login_required
def edit_order_view(request, order_id):
    message = ''

    orders = order.objects.get(id = order_id)
    if request.method == "POST":
        order_form = orderForm(request.POST, instance=orders)

        if order_form.is_valid():#then we go ahead and save the form
            order_form.save()

            message = "Changes saved successfuly"

        else:
             message = "Invalid data"
    else:#remember that if the method is a POST then the else is the defaullt as seen
        order_form = orderForm(instance=orders)

    context = {
         'form':order_form,
        'order':orders
    }
    return render(request, 'edit_order.html', context)

@login_required
def delete_order_view(request, order_id):
    orders = order.objects.get(id= order_id)

    orders.delete()

    return redirect(add_order_view)


@login_required
def add_payment_view(request):
    message = ''

    if request.method == "POST":
        payment_form= paymentForm(request.POST)

        if payment_form.is_valid():
            payment_form.save()
            messages.success (request,"payment added successfuly")


   
    payment_form = paymentForm()


    payments = payment.objects.all()

    context = {
        'form':payment_form,
        'msg':message,
        'payments':payments
        
    }

    return render(request,"add_payment.html",context)


@login_required
def edit_payment_view(request, payment_id):
     message = ''

     payments = payment.objects.get(id = payment_id)

     if request.method == "POST":
        payment_form = paymentForm(request.POST, instance=payments)
         

        if payment_form.is_valid():#then we go ahead and save the form
            payment_form.save()

            message = "Changes saved successfuly"

        else:
             message = "Invalid data"

     else:
        payment_form = paymentForm(instance=payments)

     context = {
         'form':payment_form,
        'order':payments
    }
     return render(request, 'edit_payment.html', context)


@login_required
def delete_payment_view(request, payment_id):
    payments = payment.objects.get(id= payment_id)

    payments.delete()

    return redirect(add_payment_view)

def sign_up_view(request):
    if request.method == "POST":
        sign_up_form = UserCreationForm(request.POST)

        if sign_up_form.is_valid():
            sign_up_form.save()

            message = 'User created succesfully'

        else:
            message = 'User creation failed'

    else:
        sign_up_form = UserCreationForm()

    context = {
        'form':sign_up_form
    }
    return render(request, 'registration/sign_up.html', context)
    


    


















