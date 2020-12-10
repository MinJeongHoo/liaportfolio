from django.core.management.base import BaseCommand
from works.models import WorkMaterial
from works.models import WorksModel
from works.models import WorkSize
from django.contrib.admin.utils import flatten
from workcategory.models import WorksCategoryModel


class Command(BaseCommand):

    help = "This command creates many users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", help="How many material do you want to create")

    def handle(self, *args, **options):
        arr = [
            ["2", "Room and Fantasy", "oil on canvas",
                "53cmX45.5cm", "2017", f"roomfantasy/1.jpg"],
            ["2", "Room and Fantasy", "oil on canvas",
                "53cmX45.5cm", "2017", f"roomfantasy/3.jpg"],
            ["2", "Room and Fantasy", "oil on canvas",
                "53cmX45.5cm", "2017", f"roomfantasy/4.jpg"],
            ["2", "Room and Fantasy", "oil on canvas",
                "53cmX45.5cm", "2017", f"roomfantasy/5.jpg"],
            ["2", "Room and Fantasy", "oil on canvas",
                "53cmX45.5cm", "2017", f"roomfantasy/6.jpg"],
            ["2", "Room and Fantasy", "oil on canvas",
                "53cmX45.5cm", "2017", f"roomfantasy/7.jpg"],
            ["2", "Room and Fantasy", "oil on canvas",
                "53cmX45.5cm", "2017", f"roomfantasy/8.jpg"],
            ["2", "Room and Fantasy", "oil on canvas",
                "53cmX45.5cm", "2017", f"roomfantasy/9.jpg"],
            ["2", "Room and Fantasy", "oil on canvas",
                "53cmX45.5cm", "2017", f"roomfantasy/10.jpg"],
            ["2", "Room and Fantasy", "oil on canvas",
                "53cmX45.5cm", "2017", f"roomfantasy/11.jpg"],
            ["2", "Room and Fantasy", "oil on canvas",
                "53cmX45.5cm", "2017", f"roomfantasy/12.jpg"],
            ["2", "Room and Fantasy", "oil on canvas",
                "53cmX45.5cm", "2017", f"roomfantasy/13.jpg"],
            ["2", "Room and Fantasy", "oil on canvas",
                "53cmX45.5cm", "2017", f"roomfantasy/14.jpg"],
            ["2", "Room and Fantasy", "oil on canvas",
                "53cmX45.5cm", "2017", f"roomfantasy/15.jpg"],
            ["2", "Room and Fantasy", "oil on canvas",
                "53cmX45.5cm", "2017", f"roomfantasy/16.jpg"],
            ["2", "Room and Fantasy", "oil on canvas",
                "53cmX45.5cm", "2017", f"roomfantasy/17.jpg"],
            ["2", "Room and Fantasy", "oil on canvas",
                "53cmX45.5cm", "2017", f"roomfantasy/18.jpg"],
            ["2", "Room and Fantasy", "oil on canvas",
                "53cmX45.5cm", "2017", f"roomfantasy/19.jpg"]
        ]

        for item in arr:
            print(item[2])
            category = WorksCategoryModel.objects.get(pk=item[0])
            material = WorkMaterial.objects.get(name=item[2])
            size = WorkSize.objects.get(name=item[3])
            WorksModel.objects.create(
                year=item[4], category=category, material=material, size=size, worksTitle=item[1], image=item[5])
        self.stdout.write(self.style.SUCCESS("Works created!"))
