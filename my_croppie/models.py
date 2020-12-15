from django.db import models


class Image(models.Model):
    photo = models.ImageField(upload_to='images')
    description = models.CharField(max_length=255)
    cropped_photo = models.ImageField(upload_to='images', default="")

    def __str__(self):
        return self.description
