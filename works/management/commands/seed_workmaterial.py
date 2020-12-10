from django.core.management.base import BaseCommand
from works.models import WorkMaterial


class Command(BaseCommand):

    help = "This command creates many users"

    def add_arguments(self, parser):
        parser.add_argument("--number", help="How many material do you want to create")

    def handle(self, *args, **options):
        material = [
         'oil on canvas',
         'oil and oilpastel on canvas'
        ]
        for a in material:
            WorkMaterial.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("WorkMaterial created!"))
