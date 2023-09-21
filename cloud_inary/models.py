from django.db import models
from django.utils.html import format_html
from cloudinary.models import CloudinaryField


class Language(models.Model):
    title = models.CharField(max_length=250)
    photo = CloudinaryField('image')

    def __str__(self):
        return self.title

    @property
    def image(self):
        return format_html('<img src="{}" width="50" height="50" style="border-radius: 50%" />'.format(self.photo.url))

    @property
    def picture(self):
        return self.photo.url
