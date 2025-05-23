from rest_framework import generics
from rest_framework import viewsets  # import the viewsets module from Django REST Framework, which allows creating API endpoints with minimal code for CRUD operations.
from book_app.models import Book
from .serializers import BookSerializer

class BookView(generics.ListCreateAPIView): # define a class-based view that inherits from ListCreateAPIView, which supports listing all objects and creating new ones.
    queryset = Book.objects.all() # specify the queryset to retrieve all Book objects from the database for this view.
    serializer_class = BookSerializer  # specify the serializer class to use for serializing/deserializing Book objects to/from JSON.

