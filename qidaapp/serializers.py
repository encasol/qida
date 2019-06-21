from django.contrib.auth.models import User, Group
from qidaapp.models import University, Student, Degre
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class UniversitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = University
        fields = ('full_name',)


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class DegreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Degre
        fields = '__all__'
