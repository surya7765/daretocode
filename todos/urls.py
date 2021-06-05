from todos.models import Answers
from django.urls import path
from django.urls.conf import include
from django.urls.resolvers import URLPattern

from .views import ListTodo, DetailTodo, Option, Answer

urlpatterns = [
    path('', ListTodo.as_view()),
    path('op/', Option.as_view()),
    path('ans/', Answer.as_view()),
    path('<int:pk>/', DetailTodo.as_view()),
]
