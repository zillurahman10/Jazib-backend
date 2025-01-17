from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()

router.register('order', views.OrderViewset)
router.register('order-items', views.OrderItemViewset)

urlpatterns = [
    path('', include(router.urls))
]
