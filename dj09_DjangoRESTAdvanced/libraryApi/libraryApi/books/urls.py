from django.urls import path, include
from rest_framework.routers import DefaultRouter

from libraryApi.books import views
from libraryApi.books.views import PublisherViewSet

router = DefaultRouter()  # used for generate urls dynamically
router.register('', PublisherViewSet)

urlpatterns = [
    # path('', views.index, name='index'),
    # path('books/', views.ListBookApiView.as_view(), name='books_list'),
    # path('publisher/<int:pk>/', views.PublisherDetail.as_view(), name='publisher-detail'),
    path('books/', views.ListBooksView.as_view(), name='books_list'),
    path('book/<int:pk>/', views.BookViewSet.as_view(), name='book_viewset'),
    path('publisher-links/', views.PublisherHyperlinkView.as_view(), name='publisher-links'),
    path('publishers/', include(router.urls))

]