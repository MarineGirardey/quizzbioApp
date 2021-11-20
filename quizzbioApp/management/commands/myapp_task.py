from django.core.management.base import BaseCommand
from quizzbioApp.database_script import *


class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        questions()
        answer()
        images()
