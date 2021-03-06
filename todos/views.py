from django.db import models
from django.db.models import query
from django.shortcuts import render
from rest_framework import generics


# Create your views here.

from .models import Todo, Option,Answers
from .serializers import TodoSerializer, OptionSerializer, AnswersSerializer


class ListTodo(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    # queryset1 = Option.objects.all()

    # combine = list(queryset) + list(queryset1)

    serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class Option(generics.ListCreateAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer


class Answer(generics.ListCreateAPIView):
    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer
