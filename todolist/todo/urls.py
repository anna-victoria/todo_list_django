from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<str:pk>', views.delete, name='delete')
    # <str:pk> is a parameter that will be passed to the delete function in views.py
]