from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm, Filter, FilterDate
from datetime import timedelta, datetime


def add_prod(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ProductForm()
    return render(request, 'tab/add_prod.html', {'form': form})


def index(request):
    form = Filter()
    form_date = FilterDate()

    if request.method == 'POST':

        if 'filter_seller' in request.POST:
            form = Filter()
            resp = request.POST['filter_seller']
            products = Product.objects.filter(seller__contains=resp)[::-1]  # Показать все ячейки с подстрокой resp
            return render(request, 'tab/index.html', {'products': products, 'form': form, 'form_date': form_date})

        elif 'filter_date' in request.POST:
            form_date = FilterDate()
            resp = request.POST['filter_date']
            if resp == 'WEEK':
                week_ago = datetime.now().date() - timedelta(days=7)
            elif resp == 'MONTH':
                week_ago = datetime.now().date() - timedelta(days=31)
            products = Product.objects.filter(date__gte=week_ago)[::-1]
            return render(request, 'tab/index.html', {'products': products, 'form': form, 'form_date': form_date})

    products = Product.objects.all()[::-1]
    return render(request, 'tab/index.html', {'products': products, 'form': form, 'form_date': form_date})
