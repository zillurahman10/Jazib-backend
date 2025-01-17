from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Product.urls')),  # Include your app-specific API
    path('', include('User.urls')),  # Include your app-specific API
    path('', include('Order.urls')),  # Include your app-specific API
    # path('', include('rest_framework.urls')),  # DRF's default front page
]
