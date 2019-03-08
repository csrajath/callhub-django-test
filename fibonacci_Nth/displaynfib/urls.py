from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.return_n_fib, name='return_n_fib') #home page display
]
