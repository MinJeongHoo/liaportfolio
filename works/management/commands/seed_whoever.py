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
        arr = [["5", "비오는 3월의 결혼식", "oil and oilpastel on canvas", "116.8cmX91cm", "2019", "비오는3월의_결혼식.webp"],
               ["5", "색동저고리 입은 아이", "oil and oilpastel on canvas",
                   "90.9cmX72.7cm", "2020", "색동저고리.webp"],
               ["5", "생일케이크", "oil and oilpastel on canvas",
                   "53cmX45.5cm", "2020", "생일케이크.webp"],
               ["5", "아이", "oil on canvas", "65cmX91cm", "2019", "아이.webp"],
               ["5", "어른에 갇힌 아이", "oil and oilpastel on canvas",
                "53cmX45.5cm", "2020", "어른에-갇힌-아이.webp"],
               ["5", "어린아이", "oil and oilpastel on canvas",
                "53cmX45.5cm", "2019", '어린아이.webp'],
               ["5", "울타리", "oil on canvas", "45.5cmX53cm", "2019", ""],
               ["5", "울타리", "oil on canvas", "53cmX45.5cm", "2020", ""],
               ["5", "잔칫날", "oil on canvas", "162.2cmX130.3cm", "2020", '잔칫날.webp'],
               ["5", "재롱", "oil and oilpastel on canvas",
                "100cmX80.3cm", "2019", '재롱.jpg'],
               ["5", "젊은 엄마", "oil and oilpastel on canvas",
                "116.8cmX91cm", "2020", '젊은엄마.jpg'],
               ["5", "아이스크림을 든 아이", "oil and oilpastel on canvas",
                "162.2cmX130.3cm", "2020", '아이스크림을_든아이.webp'],
               ["5", "솜사탕을 든 아이", "oil on canvas",
                "162.2cmX130.3cm", "2019", "솜사탕을_든_아이.webp"],
               ["5", "스타", "oil and oilpastel on canvas", "116.8cmX91cm", "2020", "스타.webp"]]

        for item in arr:
            print(item[3])
            category = WorksCategoryModel.objects.get(pk=item[0])
            material = WorkMaterial.objects.get(name=item[2])
            size = WorkSize.objects.get(name=item[3])
            WorksModel.objects.create(
                year=item[4], category=category, material=material, size=size, worksTitle=item[1], image=item[5])
        self.stdout.write(self.style.SUCCESS("Works created!"))

        # material = [
        #  'oil on canvas',
        #  'oil and oilpastel on canvas'
        # ]
        # for a in material:
        #     WorkMaterial.objects.create(name=a)
        #
