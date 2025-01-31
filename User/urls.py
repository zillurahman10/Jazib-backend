from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()

router.register('customers', views.CustomerViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.RegistrationViewset.as_view(), name='register'),
    path('activate/<uid64>/<token>/', views.activate, name="activate")
]
