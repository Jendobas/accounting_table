from django.shortcuts import render, redirect
from .models import Product, Deliveries
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


def home(request):
    form = Filter()
    form_date = FilterDate()

    if request.method == 'POST':

        if 'filter_seller' in request.POST:
            form = Filter()
            resp = request.POST['filter_seller']
            seller = Product.objects.filter(seller__contains=resp)  # Показать все ячейки с подстрокой resp
            return render(request, 'tab/home.html', {'deliveries': deliveries, 'form': form, 'form_date': form_date})

        elif 'filter_date' in request.POST:

            form_date = FilterDate()
            resp = request.POST['filter_date']
            if resp == 'WEEK':
                week_ago = datetime.now().date() - timedelta(days=7)
            elif resp == 'MONTH':
                week_ago = datetime.now().date() - timedelta(days=31)
            deliveries = Deliveries.objects.filter(date__gte=week_ago)[::-1]
            return render(request, 'tab/home.html', {'deliveries': deliveries, 'form': form, 'form_date': form_date})

    deliveries = Deliveries.objects.all()[::-1]
    return render(request, 'tab/home.html', {'deliveries': deliveries, 'form': form, 'form_date': form_date})


def one_delivery(request, id_delivery: int):
    delivery = Product.objects.filter(date_name_id=id_delivery)
    return render(request, 'tab/one-delivery.html', {'delivery': delivery})
