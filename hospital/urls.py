from django.urls import path
from hospital import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('', views.index, name='index')
]