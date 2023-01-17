from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.users_list),
    path('edit/<int:pk>', views.editUser),
    path('delete/<int:pk>', views.deleteUser)
]
