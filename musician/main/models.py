from django.db import models
from django.contrib.auth.models import User


class Authors(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'authors'

    def __str__(self):
        return self.name


class Genre(models.Model):
    name_genre = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'genre'

    def __str__(self):
        return self.name_genre


class Compositions(models.Model):
    name_composition = models.CharField(max_length=200)
    path = models.CharField(max_length=200, blank=True, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'compositions'

    def __str__(self):
        return self.name_composition


class Perfomances(models.Model):
    class Ideal(models.IntegerChoices):
        YES = 1
        NO = 0

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    composition = models.ForeignKey(Compositions, on_delete=models.CASCADE)
    path = models.CharField(max_length=200, blank=True, null=True)
    datetime = models.DateField()
    is_ideal = models.IntegerField(choices=Ideal.choices)

    class Meta:
        managed = False
        db_table = 'perfomances'
