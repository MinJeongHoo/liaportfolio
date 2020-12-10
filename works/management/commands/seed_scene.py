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
        arr = [["3", "경리단길 마카롱집", "oil on canvas", "45.5cmX53cm", "2018", "경리단길마카롱집.jpg"],
               ["3", "서울의 집", "oil on canvas", "116.8cmX91cm", "2018", "서울의집.jpg"],
               ["3", "여유", "oil on canvas", "116.8cmX91cm", "2018", "여유.jpg"],
               ["3", "용산 분홍 모텔", "oil on canvas",
                "45.5cmX53cm", "2018", "용산분홍호텔.jpg"],
               ["3", "화곡 상가", "oil on canvas", "45.5cmX53cm", "2018", "화곡상가.jpg"],
               ["3", "분홍 포르쉐", "oil on canvas", "45.5cmX53cm", "2018", "분홍포르쉐.jpg"],
               ["3", "빨래마르는 풍경", "oil on canvas",
                "116.8cmX91cm", "2018", "빨래마르는풍경.jpg"],
               ["3", "오래된 동네", "oil on canvas",
                   "116.8cmX80.5cm", "2018", "오래된동제.jpg"],
               ["3", "용운만화", "oil on canvas", "116.8cmX91cm", "2018", "용운만화.JPG"],
               ["3", "찾지않는 놀이터", "oil on canvas",
                   "163cmX130cm", "2019", "찾지않는_놀이터.jpg"],
               ["3", "집으로 가는 길", "oil on canvas",
                   "116.8cmX91cm", "2018", "집으로가늘길.jpg"]
               ]

        for item in arr:
            print(item[3])
            category = WorksCategoryModel.objects.get(pk=item[0])
            material = WorkMaterial.objects.get(name=item[2])
            size = WorkSize.objects.get(name=item[3])
            WorksModel.objects.create(
                year=item[4], category=category, material=material, size=size, worksTitle=item[1], image=item[5])
        self.stdout.write(self.style.SUCCESS("Works created!"))
