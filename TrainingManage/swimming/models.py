from django.db import models


class Coach(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Group(models.Model):
    name = models.CharField(max_length=200)
    capacity = models.IntegerField(null = True)
    coach = models.ForeignKey(Coach, on_delete = models.PROTECT, related_name = "groups")

    def __str__(self):
        return self.name


class Trainee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    birth_date = models.DateField(null = True)
    group = models.ForeignKey(Group, on_delete=models.PROTECT, related_name="trainees")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
