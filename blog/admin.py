from django.contrib import admin

# Register your models here.
from .models import Dj_post, Dj_category

admin.site.register(Dj_post)
admin.site.register(Dj_category)