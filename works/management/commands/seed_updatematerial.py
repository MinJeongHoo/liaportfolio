from django.core.management.base import BaseCommand
from works.models import WorkMaterial
from works.models import WorksModel
from works.models import WorkSize
from workscategory.models import WorksCategoryModel


class Command(BaseCommand):

    help = "This command creates many users"

    def add_arguments(self, parser):
        parser.add_argument("--number", help="How many material do you want to create")

    def handle(self, *args, **options):
        works = WorksModel.objects.filter(size=None,worksTitle="Room and Fantasy")
        size = WorkSize.objects.get(name="53cmX45cm")
        print(works)
        for a in works:
            a.size = size
            a.save()
        self.stdout.write(self.style.SUCCESS("Works created!"))