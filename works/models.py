from django.db import models
from core import models as core_models
from core.models import TimeStampedModel as timestamp


class AbstractItem(timestamp):

    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class WorkSize(AbstractItem):
    class Meta:
        verbose_name = "Work Size"


class WorkMaterial(AbstractItem):
    class Meta:
        verbose_name = "Work material"


class WorksModel(models.Model):

    worksTitle = models.CharField(max_length=150)
    image = models.ImageField()
    year = models.CharField(max_length=4, null=True, default="")
    category = models.ForeignKey('workcategory.WorksCategoryModel',
                                 related_name="work", on_delete=models.CASCADE, unique=False, null=True)
    material = models.ForeignKey(
        "WorkMaterial", related_name="work", on_delete=models.SET_NULL, null=True, default="")
    size = models.ForeignKey("WorkSize", related_name="work",
                             on_delete=models.SET_NULL, null=True, default="")

    def __str__(self):
        return self.worksTitle
