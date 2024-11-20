from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from libraryApi.books.models import Book
from libraryApi.books.serializers import BookSerializer


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


class ListBooksView(APIView):  # APIView is the base class same as View in Django

    def get(self, request):
        books = Book.objects.all()

        serializer = BookSerializer(books, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
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
class BookViewSet(APIView):
    @staticmethod
    def get_object(pk):
        return get_object_or_404(Book, pk=pk)

    def get(self, request, pk: int):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk: int):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk: int):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk: int):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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

