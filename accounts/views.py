from django.shortcuts import render 
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm
from .forms import CustomerForm,CreateUserForm

from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def home(request):
	customers = Customer.objects.all()
	orders = Order.objects.all()
	
	total_customers = customers.count()
	total_orders = orders.count()

	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()

	context = {'orders':orders, 'customers':customers,
	'order_count':total_orders,'total_deliverd':delivered,
	'total_pending':pending }

	return render(request, 'dashboard.html',context)

def customerList(request):
	customers = Customer.objects.all()

	context = {'customers':customers, }
	return render(request, 'customerList.html',context)

def login(request):
	return render(request, 'login.html')


def signup(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
	context={'register_form':form}
	return render(request, 'register.html',context)

def meals(request):
	meals = Meal.objects.all()
	return render(request, 'meals.html', {'meals':meals})


def customer(request, pk_test):
	customer = Customer.objects.get(id=pk_test)
	orders = customer.order_set.all()  # Returns all orders related to customer
	order_count = orders.count()

	context = {'customer':customer, 'view_customer_oders':orders, 'order_count':order_count}
	return render(request, 'customer.html',context)

def createOrder(request):
	form = OrderForm()
	if request.method == 'POST':
		form = OrderForm(request.POST)
	
		if (form.is_valid()):
			form.save()
		return redirect('/')	
	context = {'new_form':form}
	return render(request, 'order_form.html', context)
		
def createCustomer(request):
	new_form = CustomerForm()
	if request.method == 'POST':
		new_form = CustomerForm(request.POST)
		if new_form.is_valid():
			new_form.save()
		return redirect('/')
		

	context = {'customer_form':new_form}
	return render(request, 'add_customer.html', context)


def updateOrder(request, pk):

	order = Order.objects.get(id=pk)
	form = OrderForm(instance=order)

	if request.method == 'POST':
	 	form = OrderForm(request.POST, instance=order)
	 	if form.is_valid():
	 		form.save()
	 		return redirect('/')

	context = {'new_form':form}
	return render(request, 'order_form.html',context)

def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('/')

	context = {'item':order}
	return render(request, 'order_delete.html', context)