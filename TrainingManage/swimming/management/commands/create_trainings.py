import datetime

from django.core.management.base import BaseCommand

from swimming.models import Training, Group, Facility


class Command(BaseCommand):
    help = "My shiny new management command for training creation."

    # def add_arguments(self, parser):
    #     parser.add_argument('sample', nargs = '+')

    def handle(self, *args, **options):
        Facility.objects.all().delete()
        for i in range(1, 9):
            Facility.objects.create(
                description = f'Lane{i}',
                capacity = 8,
                location = "Pool, Mashabe Sade"
            )

        dt = datetime.datetime(2019, 12, 29, 13, 15)
        for idx, group in enumerate(Group.objects.all()[:10]):
            fac = Facility.objects.all().order_by('?').first()
            if idx < 5:
                for j in range(12):
                    s_dt = dt + datetime.timedelta(weeks = j, minutes = 45 * idx)
                    w_dt = dt + datetime.timedelta(weeks = j, days = 3, minutes = 45 * idx)
                    Training.objects.create(
                        group = group,
                        number = group.trainings.filter(active = True).count() + 1,
                        day = s_dt.isoweekday(),
                        start_date_time = s_dt,
                        length = 45,
                        facility = fac
                    )
                    Training.objects.create(
                        group = group,
                        number = group.trainings.filter(active = True).count() + 1,
                        day = w_dt.isoweekday(),
                        start_date_time = w_dt,
                        length = 45,
                        facility = fac
                    )

            else:
                for j in range(12):
                    s_dt = dt + datetime.timedelta(weeks = j, days =1, minutes = 45 * idx)
                    w_dt = dt + datetime.timedelta(weeks = j, days = 4, minutes = 45 * idx)
                    Training.objects.create(
                        group = group,
                        number = group.trainings.filter(active = True).count() + 1,
                        day = s_dt.isoweekday(),
                        start_date_time = s_dt,
                        length = 45,
                        facility = fac
                    )
                    Training.objects.create(
                        group = group,
                        number = group.trainings.filter(active = True).count() + 1,
                        day = w_dt.isoweekday(),
                        start_date_time = w_dt,
                        length = 45,
                        facility = fac
                    )

