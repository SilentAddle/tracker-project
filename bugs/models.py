from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Bugs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    date_post = models.DateTimeField(blank=True, null=True, default=timezone.now)
    completed = models.IntegerField(default="0")
    image = models.ImageField(upload_to='images', blank=True, null=True)
    credits = models.IntegerField(default="0")