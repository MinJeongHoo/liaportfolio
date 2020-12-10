from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.WorksModel)
class WorksAdmin(admin.ModelAdmin):
    list_display = (
        "worksTitle",
        "year",
        'category',
        'material',
        'size'
    )
    list_filter = ("category", "material", "size")
    search_fields = ("^worksTitle",)


@admin.register(models.WorkSize)
class WorksSizeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


@admin.register(models.WorkMaterial)
class WorksMaterialAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
