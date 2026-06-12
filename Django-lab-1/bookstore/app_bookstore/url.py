from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('books/', views.book, name='books'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/update/<str:isbn>', views.add_book, name='update_book'),
    path('book/<str:isbn>', views.book, name='book'),
    path('books/delete/<str:isbn>', views.delete, name='delete'),
]