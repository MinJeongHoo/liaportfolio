from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.WorksCategoryModel)
class WorksCategoryAdmin(admin.ModelAdmin):
    list_display = ("category",)
