from django.db import models

class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    portfolio_image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title
