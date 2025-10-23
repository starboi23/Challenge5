from django.db import models


class Hobby(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    hobby_image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title