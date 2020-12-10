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
        arr = [["6", "미키마우스", "23cmX16cm", "oil and oilpastel on canvas", "2020", "미키마우스.JPG"],
               ["6", "소녀 시리즈", "90.9cmX72.7cm",
                   "oil and oilpastel on canvas", "2020", "소녀시리즈.jpg"],
               ["6", "소녀시리즈", "33cmX45.5cm", "oil on canvas", "2020", "소녀시리즈2.jpg"],
               ["6", "이상한 나라의 앨리스", "23cmX16cm", "oil and oilpastel on canvas",
                   "2020", "이상한나라의_엘리스.JPG"],
               ["6", "피터팬", "23cmX16cm",
                   "oil and oilpastel on canvas", "2020", "피터펜.JPG"],
               ["6", "헬로 키티", "23cmX16cm",
                   "oil and oilpastel on canvas", "2020", "헬로키티.JPG"]
               ]

        for item in arr:
            print(item[2])
            category = WorksCategoryModel.objects.get(pk=item[0])
            material = WorkMaterial.objects.get(name=item[3])
            size = WorkSize.objects.get(name=item[2])
            WorksModel.objects.create(
                year=item[4], category=category, material=material, size=size, worksTitle=item[1], image=item[5])
        self.stdout.write(self.style.SUCCESS("Works created!"))
