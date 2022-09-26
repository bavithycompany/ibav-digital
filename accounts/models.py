from django.db import models


class Prospect(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    telephone = models.CharField(max_length=20, default='-------------')

    def __str__(self):
        return self.username


class Contacteur(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    content = models.TextField()
    telephone = models.CharField(max_length=20, default='-------------')

    def __str__(self):
        return self.username
