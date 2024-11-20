from django.urls import path

from libraryApi.books import views

urlpatterns = [
    # path('', views.index, name='index'),
    # path('books/', views.ListBookApiView.as_view(), name='books_list'),
    path('books/', views.ListBooksView.as_view(), name='books_list'),
    path('book/<int:pk>/', views.BookViewSet.as_view(), name='book_viewset'),
]