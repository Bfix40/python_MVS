from rest_framework.routers import DefaultRouter
from .views import UserViewSet, JobViewSet

router = DefaultRouter()

router.register(r'/users', UserViewSet, basename='users')

router.register(r'/jobs', JobViewSet, basename='jobs')
