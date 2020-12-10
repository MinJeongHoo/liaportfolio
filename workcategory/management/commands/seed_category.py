from django.core.management.base import BaseCommand
from workcategory.models import WorksCategoryModel


class Command(BaseCommand):

    help = "This command creates many users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", help="How many category do you want to create")

    def handle(self, *args, **options):
        material = [
            '냉소적 긍정',
            'Room and Fantasy',
            'Scene and Fantasy',
            'Object and Fantasy',
            '그때 누구나였던',
            '윤곽',
            'Drawing'
        ]
        for a in material:
            WorksCategoryModel.objects.create(category=a)
        self.stdout.write(self.style.SUCCESS("WorksCategoryModel created!"))
