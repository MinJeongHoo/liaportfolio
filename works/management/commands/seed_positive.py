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
        arr = [["1", "Dreamer", "oil on canvas",  "116.8cmX91cm", "2016", "dreamer.jpg"],
               ["1", "Poor pure", "oil on canvas",
                   "116.8cmX91cm", "2016", "poorpure.jpg"],
               ["1", "사랑은 어디에 있는가", "oil on canvas",
                   "116.8cmX91cm", "2016", "사랑은어디에있는가.jpg"],
               ["1", "인생은아름다워", "oil on canvas",
                "116.8cmX91cm", "2016", "인생은아름다워.jpg"],
               ["1", "20대를 기념하기위해 그린 그림", "oil on canvas",
                "90.9cmX72.7cm", "2017", "20대를기념하기위해그린그림.JPG"],
               ["1", "adulthood", "oil on canvas",
                "91cmX116.8cm", "2016", "adulthood.jpg"],
               ["1", "가치있는 빈곤",  "oil on canvas",
                   "116.8cmX91cm", "2017", "가치있는빈곤.JPG"],
               ["1", "수평의기준", "oil on canvas", "106cmX41.3cm", "2018", "수평의기준.jpg"],
               ["1", "시시한 이유에서의 환희", "oil on canvas",
                "162.2cmX130.3cm", "2018", "이유에서의환희.jpg"]
               ]

        for item in arr:
            print(item[2])
            category = WorksCategoryModel.objects.get(pk=item[0])
            material = WorkMaterial.objects.get(name=item[2])
            size = WorkSize.objects.get(name=item[3])
            WorksModel.objects.create(
                year=item[4], category=category, material=material, size=size, worksTitle=item[1], image=item[5])
        self.stdout.write(self.style.SUCCESS("Works created!"))
