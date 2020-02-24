from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Coach(models.Model):
    user = models.OneToOneField(User, on_delete = models.PROTECT)
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    gender = models.CharField(max_length = 200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Group(models.Model):
    class Level(models.IntegerChoices):
        PRE_SWIM = 1, _('Pre_swim'),
        BEGGINERS = 2, _('Begginers'),
        ADVANCED = 3, _('Advanced'),
        COMPETATIVE = 4, _('Competative')

    class AgeGroup(models.IntegerChoices):
        FIVE_TO_SEVEN = 1, _('5-7')
        EIGHT_TO_TWELVE = 2, _('8-12')
        THIRTEEN_TO_EIGHTEEN = 3, _('13-18')
        ABOVE_EIGHTEEN = 4, _('18+')

    name = models.CharField(max_length = 200)
    capacity = models.IntegerField(null = True)
    level = models.IntegerField(choices = Level.choices)
    age_group = models.IntegerField(choices = AgeGroup.choices)
    coach = models.ForeignKey(Coach, on_delete = models.PROTECT, related_name = "groups")

    def __str__(self):
        return self.name.title()


class Trainee(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 30)
    gender = models.CharField(max_length = 20)
    birth_date = models.DateField(null = True)
    group = models.ForeignKey(Group, on_delete = models.PROTECT, related_name = "trainees")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Facility(models.Model):
    description = models.CharField(max_length = 200)
    capacity = models.IntegerField()
    location = models.CharField(max_length = 200)

    def __str__(self):
        return self.description


class AdminSlot(models.Model):
    title = models.CharField(max_length = 200)
    facility = models.ForeignKey(Facility, on_delete = models.PROTECT, related_name = "admin_slots")
    start_date_time = models.DateTimeField()
    length = models.IntegerField(default = 45)


class Training(models.Model):
    group = models.ForeignKey(Group, on_delete = models.PROTECT, related_name = "trainings")
    number = models.IntegerField()
    content = models.TextField()
    day = models.IntegerField()
    start_date_time = models.DateTimeField()
    length = models.IntegerField(default = 45)
    facility = models.ForeignKey(Facility, on_delete = models.PROTECT, related_name = "trainings")
    active = models.BooleanField(default = True)
