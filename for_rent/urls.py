"""
URL configuration for for_rent project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path

from authApi.views import authiView
from property_api.views import PropertyClassViewSet
from reviews_api.views import ReviewDetail, ReviewList
from rest_framework.routers import DefaultRouter
from django.urls import path
from rest_framework.routers import DefaultRouter
from authApi.views import authiView, LoginView

router = DefaultRouter()
router.register(r'allpropertiess', PropertyClassViewSet, basename='allpropertiess')
router.register(r'register', authiView, basename='register')
router.register(r'authi', authiView, basename='authi')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('reviews/', ReviewList.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    path('login/', LoginView.as_view(), name='login'),
    path('', include(router.urls)),
]
