from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('productos/', views.index, name='productos'), 
]