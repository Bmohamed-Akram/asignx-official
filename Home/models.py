from django.db import models

# Create your models here.

class project(models.Model):
    client = models.CharField(max_length=300)
    service = models.CharField(max_length=300)
    image = models.ImageField()
    image2 = models.ImageField()
    description = models.CharField(max_length=2000)
    link = models.URLField()

class client_logo(models.Model):
    logo = models.ImageField()
    name = models.CharField(max_length=150)

class client_feedback(models.Model):
    feedback = models.TextField()
    name = models.CharField(max_length=150)
    image = models.ImageField()
    position = models.CharField(max_length=150)


class contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=350)
    message = models.TextField(max_length=3000)

class subscribe(models.Model):
    email = models.EmailField()

class about_count(models.Model):
    coc = models.IntegerField()
    pc = models.IntegerField()
    hc = models.IntegerField()
    collab = models.IntegerField()