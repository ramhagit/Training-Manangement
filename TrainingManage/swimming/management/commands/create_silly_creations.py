import random

import silly

from django.core.management.base import BaseCommand
from swimming.models import Coach, Group, Trainee


class Command(BaseCommand):
    help = "Create some silly creations."

    def add_arguments(self, parser):
        parser.add_argument('n', type=int)

    def handle(self, n, *args, **options):
        for i in range(3):
            o = Coach.objects.create(first_name = silly.name(), last_name = silly.name(), gender = silly.gender())
            o.save()

        coaches = Coach.objects.all()

        for i in range(13):
            o = Group(
                name = silly.name(),
                capacity = random.uniform(8, 20),
                coach = random.choice(coaches))
            o.save()

        groups = Group.objects.all()

        for i in range(n):
            o = Trainee.objects.create(
                first_name = silly.name(),
                last_name = silly.name(),
                gender = silly.gender(),
                birth_date = silly.datetime(),
                group = random.choice(groups)
            )
            o.save()