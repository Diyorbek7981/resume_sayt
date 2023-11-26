from django.db import models
from django.urls import reverse


# Create your models here.

# class HomeModel(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='home/')
#
#     def __str__(self):
#         return self.title


class AboutModel(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='home/')
    bio = models.TextField(null=True, blank=True)
    dirth = models.DateField()
    adres = models.CharField(max_length=222)
    code = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    proect = models.IntegerField()

    def __str__(self):
        return self.name


class ResumeModel(models.Model):
    year = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    # icons= (
    #     (ANALY,'analysis'),
    # )


ICON_CHOICES = (
    ('analysis', "analysis"),
    ('flasks', 'flasks'),
    ('ideas', 'ideas')
)


class ServisModel(models.Model):
    icon = models.CharField(max_length=50, choices=ICON_CHOICES)
    profession = models.CharField(max_length=50)

    def __str__(self):
        return self.profession


class SkilModel(models.Model):
    skil_name = models.CharField(max_length=50)
    percent = models.IntegerField()

    def __str__(self):
        return self.skil_name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
