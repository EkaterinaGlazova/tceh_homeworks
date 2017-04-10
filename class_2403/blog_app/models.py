from django.db import models


# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=30)
    message = models.CharField(max_length=150)

    def __str__(self):
        return self.message


