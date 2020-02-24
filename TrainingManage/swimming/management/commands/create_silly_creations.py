import random

import silly
from django.contrib.auth.models import User

from django.core.management.base import BaseCommand
from swimming.models import Coach, Group, Trainee


class Command(BaseCommand):
    help = "Create some silly creations."

    def add_arguments(self, parser):
        parser.add_argument('n', type = int)

    def handle(self, n, *args, **options):
        o1, c1 = Coach.objects.get_or_create(user_id=2, first_name = 'Nuni', last_name = 'Shasha', gender = 'Male')
        o1.save()
        o2, c2 = Coach.objects.get_or_create(user_id=3, first_name = 'Avi', last_name = 'Yitzhaki', gender = 'Male')
        o2.save()
        o3, c3 = Coach.objects.get_or_create(user_id=4, first_name = 'Shira', last_name = 'Lulu', gender = 'Female')
        o3.save()

        coaches = Coach.objects.all()

        groups_names = ['fishies', 'goldfish', 'jellyfish', 'octopus', 'squid', 'dolphin', 'pre_masters', 'masters',
                        'provision', 'team']
        levels = [1, 1, 1, 2, 2, 3, 3, 4, 4, 4]
        age_groups = [1, 1, 2, 2, 3, 2, 4, 4, 2, 3]

        for i in range(10):
            o, c = Group.objects.get_or_create(
                name = groups_names[i],
                level = levels[i],
                age_group = age_groups[i],
                coach = random.choice(coaches),
                defaults = {
                    'capacity': random.uniform(8, 20)
                })

        groups = Group.objects.all()

        for i in range(n):
            o = Trainee.objects.create(
                first_name = silly.name().split(' ')[0],
                last_name = silly.name().split(' ')[0],
                gender = silly.gender(),
                birth_date = silly.datetime().date(),
                group = random.choice(groups)
            )
            o.save()
