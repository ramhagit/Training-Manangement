from django.db import models


class Coach(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Group(models.Model):
    class Level(models.IntegerChoices):
        Pre_swim = 1
        begginers = 2
        advanced = 3
        competative = 4

    class AgeGroup(models.IntegerChoices):
        five_to_seven = 1, '5-7'
        eight_to_twelve = 2, '8-12'
        thirteen_to_eighteen = 3, '13-18'
        above_eighteen = 4, '18+'
        __empty__ = '(Unknown)'

    name = models.CharField(max_length=200)
    capacity = models.IntegerField(null = True)
    level = models.IntegerField(choices=Level.choices)
    age_group = models.IntegerField(choices=AgeGroup.choices)
    coach = models.ForeignKey(Coach, on_delete = models.PROTECT, related_name = "groups")

    def __str__(self):
        return self.name.title()


class Trainee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    birth_date = models.DateField(null = True)
    group = models.ForeignKey(Group, on_delete=models.PROTECT, related_name = "trainees")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
