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
            ["7", "Drawing", "", "", "", f"drawing/1.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/2.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/3.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/4.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/5.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/6.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/7.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/8.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/9.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/10.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/11.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/12.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/13.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/14.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/15.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/16.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/17.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/18.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/19.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/20.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/21.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/22.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/23.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/24.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/25.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/26.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/27.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/28.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/29.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/30.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/31.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/32.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/33.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/34.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/35.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/36.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/37.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/38.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/39.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/40.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/41.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/42.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/43.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/44.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/45.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/46.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/47.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/48.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/49.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/50.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/51.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/52.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/53.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/54.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/55.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/56.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/57.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/58.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/59.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/60.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/61.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/62.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/63.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/64.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/65.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/66.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/67.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/68.jpg"],
            ["7", "Drawing", "", "", "", f"drawing/69.jpg"]
        ]

        for item in arr:
            category = WorksCategoryModel.objects.get(pk=item[0])
            WorksModel.objects.create(
                category=category, worksTitle=item[1], image=item[5])
        self.stdout.write(self.style.SUCCESS("Works created!"))
