from django.core.management.base import BaseCommand
from works.models import WorkSize


class Command(BaseCommand):

    help = "This command creates many users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", help="How many size do you want to create")

    def handle(self, *args, **options):
        size = [
            '53cmX45.5cm',
            '90.9cmX72.7cm',
            '100cmX80.3cm',
            '116.8mX91cm',
            '162.2cmX130.3cm'
        ]
        for a in size:
            WorkSize.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("WorkSize created!"))
