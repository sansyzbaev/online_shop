from django.urls import path
from landing import views

urlpatterns = [
    path('products/', views.landing, name='products'),
]