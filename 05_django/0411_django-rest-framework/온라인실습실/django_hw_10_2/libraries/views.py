from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import render
from .models import Book
from .serializers import BookListSerializer, BookSerializer

@api_view(['GET'])
def library_list(request):
  books = Book.objects.all()
  serializer = BookSerializer(books, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def detail(request, pk):
  book = Book.objects.get(pk=pk)
  serializer = BookListSerializer(book)
  return Response(serializer.data)