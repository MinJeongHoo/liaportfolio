from django.db import models

# Create your models here.


class WorksCategoryModel(models.Model):

    category = models.CharField(max_length=40, default=None)
    description = models.TextField()

    def __str__(self):
        return self.category
