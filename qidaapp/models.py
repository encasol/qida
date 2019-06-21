from django.db import models


class University(models.Model):
    full_name = models.CharField(
        max_length=100,
        verbose_name='university full name'
    )


class Student(models.Model):
    first_name = models.CharField('first name', max_length=30)
    last_name = models.CharField('last name', max_length=30)

    university = models.ForeignKey(
        University,
        on_delete=models.CASCADE,
    )


class Degre(models.Model):
    name = models.CharField('degre name', max_length=30)
    field = models.CharField('degre field', max_length=30)

    university = models.ForeignKey(
        University,
        on_delete=models.CASCADE,
    )

    participants = models.ManyToManyField(
        Student
    )
