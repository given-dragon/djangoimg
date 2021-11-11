from django import urls
from django.urls import include,path
from rest_framework import routers, urlpatterns
from rest_framework.routers import DefaultRouter
from .views import ImageView

router =DefaultRouter()
router.register('upload', ImageView)

urlpatterns = [
    path('',include(router.urls)),
]