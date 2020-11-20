from django.contrib import admin
from .models import UserFile, UserProfile


admin.site.register(UserProfile)
admin.site.register(UserFile)

