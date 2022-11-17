from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.utils import html

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer, BookMiniSerializer


class Another(View):

    def get(self, request):
        books = Book.objects.filter(is_published=True)
        return HttpResponse("<br><br>".join([html.escape(book.__dict__) for book in books]))


def first(request):
    books = Book.objects.all()
    return render(request, 'first_temp.html', {'data': 'this is some data', 'books': books})


class MiniBookViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BookMiniSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = BookSerializer(instance)
        return Response(serializer.data)


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
