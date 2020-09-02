from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login),
    path('signup/', views.signup),
    path('meals/',views.meals, name="goto_foods_page"),
    path('customerList/',views.customerList, name="customer_list_page"),
    path('customer/<str:pk_test>/', views.customer, name="customer_info"),  
    path('create_order/', views.createOrder, name="create_new_order"),
    path('new_customer/', views.createCustomer, name="new_customer"),
    path('create_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),

]