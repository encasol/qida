from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from qidaapp import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'universities', views.UniversityViewSet)
router.register(r'students', views.StudentViewSet)
router.register(r'degre', views.DegreViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(
        'api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    )
]
