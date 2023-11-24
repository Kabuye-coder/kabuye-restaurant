"""
URL configuration for restaurant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include #the include helps us to include files from another file
from django.conf import settings
from django.conf.urls.static import static
from mambo.views import* 




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index_page'),
    path('sign_up/', sign_up_view, name='sign_up_page'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('home/', home_view, name='home_page'),
    path('contact/', contact_view, name='contact_page'),
    path('foodyard/', foodyard_view, name='foodyard_page'),
    path('add_category/', add_category_view, name='add_category_page'),
    path('add_dish/',add_dish_view,name= 'add_dish_page'),
    path('add_customer/', add_customer_view, name= 'add_customer_page'),
    path('add_order/', add_order_view, name= 'add_order_page'),
    path('add_payment/', add_payment_view, name= 'add_payment_page'),
    path('edit_category /<int:category_id>/', edit_category_view, name= 'edit_category_page'),
    path('delete_category /<int:category_id>/',delete_category_view, name = 'delete_category_page'),
    path('edit_customer /<int:customer_id>/', edit_customer_table_view, name= 'edit_customer_page'),
    path('delete_customer /<int:customer_id>/',delete_customer_table_view, name = 'delete_customer_page'),
    path('edit_dish /<int:dish_id>/', edit_dish_view, name= 'edit_dish_page'),
    path('delete_dish /<int:dish_id>/',delete_dish_view, name = 'delete_dish_page'),
    path('edit_order /<int:order_id>/', edit_order_view, name= 'edit_order_page'),
    path('delete_order /<int:order_id>/',delete_order_view, name = 'delete_order_page'),
    path('edit_payment /<int:payment_id>/', edit_payment_view, name= 'edit_payment_page'),
    path('delete_payment /<int:payment_id>/',delete_payment_view, name = 'delete_payment_page')



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
