from django.db import models


class Bank(models.Model):
    name = models.CharField(max_length=225)
    code = models.CharField(max_length=10)
    address = models.TextField()

    def __str__(self):
        return self.name
