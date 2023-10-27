from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_prod),
    path('', views.home),
    path('delivery/<int:id_delivery>', views.one_delivery, name='delivery_detail'),
]