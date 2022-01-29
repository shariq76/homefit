from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.TextField()
    address = models.TextField()
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30, default='Kerala')
    country = models.CharField(max_length=30, default='India')

    def __str__(self):
        return self.user.username

class FeedBack(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=250)
    feedback = models.TextField()

    def __str__(self):
        return "#" + str(self.user.id) + " " + self.name
