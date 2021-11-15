from django.contrib import admin
from .models import Companies, Sales, Products

# Register your models here.
admin.site.register(Companies)
admin.site.register(Sales)
admin.site.register(Products)