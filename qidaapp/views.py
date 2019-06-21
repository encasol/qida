from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from qidaapp.models import University, Student, Degre
from qidaapp.serializers import UserSerializer
from qidaapp.serializers import GroupSerializer
from qidaapp.serializers import StudentSerializer
from qidaapp.serializers import UniversitySerializer
from qidaapp.serializers import DegreSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class UniversityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows universities to be viewed or edited.
    """
    queryset = University.objects.all()
    serializer_class = UniversitySerializer


class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows universities to be viewed or edited.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class DegreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows universities to be viewed or edited.
    """
    queryset = Degre.objects.all()
    serializer_class = DegreSerializer
