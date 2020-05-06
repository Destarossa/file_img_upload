from django.db import models
from cloudinary.models import CloudinaryField


class FileModel(models.Model):
    title = models.CharField(max_length=100, blank=True, default="image")

    fileup = models.FileField(upload_to='new')

    def __str__(self):
        return self.title


class ImageModel(models.Model):
    imgTitle = models.CharField(max_length=100, blank=True)
    image = CloudinaryField('image')
