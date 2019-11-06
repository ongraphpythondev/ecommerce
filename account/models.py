from django.contrib.auth.models import User
from django.db import models



class User(User):
    mobile = models.CharField(max_length=10)
    # pincode= models.IntegerField(max_length=7)
    def __str__(self):
        return self.first_name

