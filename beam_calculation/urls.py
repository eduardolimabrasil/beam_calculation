from rest_framework.routers import DefaultRouter
from django.conf.urls import url
from django.urls import include
from django.contrib import admin
from calculation.views import BeamCalculationView

router = DefaultRouter(trailing_slash=False)
router.register(r'calculation', BeamCalculationView)

urlpatterns = [
    url(r'', include(router.urls))
]
