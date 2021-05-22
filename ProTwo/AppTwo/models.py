from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email_addr = models.EmailField(max_length=40)
