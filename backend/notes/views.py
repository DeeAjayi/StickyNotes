from django.shortcuts import render

from rest_framework import viewsets
from .serializers import NotesSerializer
from .models import Notes


class NotesView(viewsets.ModelViewSet):
	serializer_class = NotesSerializer
	queryset = Notes.objects.all()


