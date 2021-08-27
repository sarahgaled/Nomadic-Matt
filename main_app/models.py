from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

class Blog(models.Model):
    place = models.CharField(max_length=200)
    date = models.DateField("Trip date")
    description = models.TextField(max_length=450)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.place

    def get_absolute_url(self):
        return reverse("blogs_detail", kwargs={"blog_id": self.id})
    
class Photo(models.Model):
    url = models.CharField(max_length=250)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for blog_id: {self.blog_id} @{self.url}"
