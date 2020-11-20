from django.contrib.auth.models import User
from django.db import models


# model for user
class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=35)

    def __str__(self):
        return self.name


# model for files to be saved
class UserFile(models.Model):
    name = models.CharField(max_length=20)
    pdf = models.FileField(upload_to='pdf_folder')  # files will be saved in pdf_folder in root directory

    def __str__(self):
        return self.name
