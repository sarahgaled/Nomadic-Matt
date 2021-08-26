from django.db import models
from django.urls import reverse

# Create your models here.

class Blog(models.Model):
    place = models.CharField(max_length=200)
    description = models.TextField(max_length=450)
    date = models.DateField()

    def __str__(self):
        return self.place

    def get_absolute_url(self):
        return reverse("blogs_detail", kwargs={"blog_id": self.id})
    
