from django.core.management.base import BaseCommand
from works.models import WorkMaterial
from works.models import WorksModel
from works.models import WorkSize
from workcategory.models import WorksCategoryModel


class Command(BaseCommand):

    help = "This command creates many users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", help="How many material do you want to create")

    def handle(self, *args, **options):
        arr = [["4", "라디오",  "oil on canvas", "45.5cmX53cm", "2018", "라디오.jpg"],
               ["4", "가족을 닮은 식탁", "oil on canvas",
                   "162.2cmX130.3cm", "2018", "가족을닮은식탁.jpg"],
               ["4", "모자", "oil on canvas",  "45.5cmX53cm", "2018", "모자.jpg"],
               ["4", "복돼지", "oil on canvas", "45.5cmX53cm", "2019", "복돼지.jpg"]
               ]

        for item in arr:
            print(item[3])
            category = WorksCategoryModel.objects.get(pk=item[0])
            material = WorkMaterial.objects.get(name=item[2])
            size = WorkSize.objects.get(name=item[3])
            WorksModel.objects.create(
                year=item[4], category=category, material=material, size=size, worksTitle=item[1], image=item[5])
        self.stdout.write(self.style.SUCCESS("Works created!"))
