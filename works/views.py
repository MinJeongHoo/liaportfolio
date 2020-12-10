from django.shortcuts import render
from . import models
from workcategory.models import WorksCategoryModel
# Create your views here.


def worksview(request, pk=0):
    category = WorksCategoryModel.objects.all().order_by('pk')
    categoryDec = ""
    works = ""

    if pk is not 0:
        try:
            categoryDec = WorksCategoryModel.objects.get(pk=pk)
            works = models.WorksModel.objects.filter(category=pk)
        except WorksCategoryModel.DoesNotExist:
            works = ""
            categoryDec = ""
    return render(request, "works.html", {"category": category, "works": works, "categoryDec": categoryDec})
