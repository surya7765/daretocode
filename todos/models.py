from django.db import models
from django.conf import settings
from audiofield.fields import AudioField
import os.path


# Create your models here.

# audio_file = AudioField(upload_to='your/upload/dir', blank=True,
#                         ext_whitelist=(".mp3", ".wav", ".ogg"),
#                         help_text=("Allowed type - .mp3, .wav, .ogg"))

class Option(models.Model):
    option = models.CharField(max_length=100)


class Answers(models.Model):
    answer = models.CharField(max_length=100)


class Todo(models.Model):
    options = models.ManyToManyField(Option)
    audio = models.FileField(upload_to='audio', max_length=100, blank=True)
    answer = models.ManyToManyField(Answers)
    created_on = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.options
