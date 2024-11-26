from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from libraryApi.books.models import Book, Publisher
from libraryApi.books.permissions import IsBookOwner
from libraryApi.books.serializers import BookSerializer, PublisherHyperlinkSerializer, PublisherSerializer, \
    BookSimpleSerializer


# Django REST
@api_view(['GET', 'POST'])
def list_books_view(request):
    if request.method == 'GET':
        books = Book.objects.all()

        serializer = BookSerializer(books, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @extend_schema - For Swagger
@extend_schema(
    request=BookSerializer,
    responses={201: BookSerializer, 400: BookSerializer}
)
class ListBooksView(ListAPIView):  # APIView is the base class same as View in Django
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


# @extend_schema - For Swagger
@extend_schema(
    request=BookSerializer,
    responses={201: BookSerializer, 400: BookSerializer}
)
class BookViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSimpleSerializer
    permission_classes = [IsAuthenticated, IsBookOwner]
    authentication_classes = ['TokenAuthentication']


# class PublisherDetail(RetrieveAPIView):
#     queryset = Publisher.objects.all()
#     serializer_class = PublisherSerializer


class PublisherViewSet(ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """


class PublisherHyperlinkView(ListAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherHyperlinkSerializer


# For the next time
# class ListBookApiView(ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# # This is how we will make it without django REST
# def list_books_view(request):
#     books = Book.objects.all()
#
#     context = {
#         'books': books
#     }
#
#     return render(request, 'some_template', context)


# # Option without rest_framework
# def list_books_view(request):
#     books = Book.objects.all()
#
#     context = {
#         'books': books
#     }
#
#     return JsonResponse(context)  # TO DO: Parse the text to Json


# # JsonResponse example
# def index(request):
#     return JsonResponse({"name": "vlado"})


"""

Django MPA(Multi Page App) SSR

books/                  - Read List     - GET
book/add               - Read Details  - GET
book/<int:pk>/details  - Create        - GET / POST
book/<int:pk>/edit     - Update        - GET / POST
book/<int:pk>/delete   - Delete        - GET / POST

-----

Django REST

books/                  - Read List     - GET
book/<int:pk>/          - Update, Create, Details, Delete
                        - PUT,    POST,   GET,    DELETE
                        
"""

