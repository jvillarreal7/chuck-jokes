from django.db import models

class Quote(models.Model):
    content = models.TextField()
