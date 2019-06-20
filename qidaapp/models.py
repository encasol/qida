from django.db.models import Model, CharField, Index, ForeignKey, CASCADE
from django.urls import reverse


class University(Model):
    full_name = CharField(
        max_length=100,
        verbose_name='university full name',
    )

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse('university_detail', args=[str(self.id)])

class Student(Model):
    first_name = CharField('first name', max_length=30)
    last_name = CharField('last name', max_length=30)
    university = ForeignKey(
        University,
        on_delete = CASCADE,
        related_name='students',
        related_query_name='person',
    )

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('student_detail', args=[str(self.id)])
