from django.urls import path
from landing import views

urlpatterns = [
    path('orders/', views.landing, name='orders'),
]