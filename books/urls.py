from django.urls import path
from .views import BookDetailView, BookListView, BookCreateView, BookListAPI, BookCreateAPI

urlpatterns = [
    path('', BookListView.as_view(), name='book-list'),
    path('<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('add/', BookCreateView.as_view(), name='book-add'),
    path('api/books/', BookListAPI.as_view(), name='api-book-list'),
    path('api/books/add/', BookCreateAPI.as_view(), name='api-book-add'),
]