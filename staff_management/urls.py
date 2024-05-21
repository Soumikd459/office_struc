from django.urls import path , include
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()

router.register('api',StaffViewset, basename= 'staff')

urlpatterns = [
   path(' ',include(router.urls)),
   path('auth/',include('rest_Framework.urls', namespace = 'rest_Framework'))
]
