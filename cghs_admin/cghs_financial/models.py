from __future__ import unicode_literals

from django.db import models


class Tag(models.Model):

    name = models.CharField(null=False, blank=False, max_length=20, unique=True)
    color = models.CharField(null=False, blank=False, max_length=7, unique=True)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class Expense(models.Model):

    value = models.DecimalField(
        null=False, blank=False, decimal_places=2, max_digits=5)
    description = models.CharField(null=False, blank=False, max_length=50)
    date = models.DateField(null=False, blank=False)
    tags = models.ManyToManyField(Tag)

    class Meta:
        verbose_name = "Expense"
        verbose_name_plural = "Expenses"
