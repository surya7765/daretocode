from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Todo, Option


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option


class TodoSerializer(serializers.ModelSerializer):

    # options = OptionSerializer(read_only=True, many=True)

    class Meta:
        fields = (
            'id',
            'options',
            'audio',
        )
        model = Todo
