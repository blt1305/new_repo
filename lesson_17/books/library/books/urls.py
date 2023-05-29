from django.urls import path

from . import views

urlpatterns = [
    path('/', views.books, name="book"),
    path('/create', views.create_book),
]