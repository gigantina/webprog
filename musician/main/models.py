from django.db import models


class Authors(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'authors'


class Compositions(models.Model):
    name_composition = models.CharField(max_length=200)
    path = models.CharField(max_length=200, blank=True, null=True)
    genre_id = models.IntegerField()
    author_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'compositions'


class Genre(models.Model):
    name_genre = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'genre'


class Perfomances(models.Model):
    user_id = models.IntegerField()
    path = models.CharField(max_length=200, blank=True, null=True)
    datetime = models.DateField()

    class Meta:
        managed = False
        db_table = 'perfomances'

