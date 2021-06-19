from django.db import models

class Joke(models.Model):
    content = models.TextField()
