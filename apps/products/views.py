from django.shortcuts import render, redirect
from apps.products.models import Product
from datetime import datetime

def home(request):

	Producks = Product.objects.all().order_by('-id')


	if 'errors' in request.session:
		errors = request.session['errors']
	else:
		errors = []

	content = {
		'products': Producks,
		'errors': errors
	}
	request.session['errors'] = []
	return render(request, 'home.html', content)

def create(request):
	array = []
	if request.POST['product_name'] == '':
		array.append('Product name cannot be blank')
		print array
	if request.POST['price'] == '':
		array.append('Price cannot be left blank')
		print array
	if request.POST['description'] == '':
		array.append('Description cannot be left blank')
		print array
	request.session['errors'] = array
	if len(array) == 0:
		Product.objects.create(brand = request.POST['brand'], product_name = request.POST['product_name'], price = request.POST['price'], description = request.POST['description'], created_at = datetime.now())
	return redirect(home)

def destroy(request, id):
	Product.objects.get(id=id).delete()
	return redirect(home)

def show(request, id):
	P = Product.objects.get(id=id)
	content = {
		'product': P,
	}

	return render(request, 'show.html', content)

def update(request, id):

	P = Product.objects.get(id=id)
	P.brand = request.POST['brand']
	P.product_name = request.POST['product_name']
	P.price = request.POST['price']
	P.description = request.POST['description']
	P.save()

	return redirect(home)