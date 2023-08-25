from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse


class Product(models.Model):
    seller = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.PositiveBigIntegerField()

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
