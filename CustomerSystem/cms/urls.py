from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"), # Home Page
    path("new", views.create, name="create"), # Create an Employee page
    path("users", views.create, name="newUser"), # API Route for managing customers (POST/DELETE handler in views.create)
]