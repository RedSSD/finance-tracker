from django.db import models


class Payment(models.Model):

    title = models.CharField(max_length=200)
    amount = models.DecimalField()
    datetime = models.DateTimeField()