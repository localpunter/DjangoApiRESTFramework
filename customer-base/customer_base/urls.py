"""customer_base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from core.views import (
    CustomerViewSet,
    ProfessionViewSet,
    DataSheetViewSet,
    DocumentViewSet,
    )

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('customers', CustomerViewSet, base_name = "customer")
router.register('professions', ProfessionViewSet, base_name = "profession")
router.register('data-sheet', DataSheetViewSet, base_name = "data_sheet")
router.register('documents', DocumentViewSet, base_name = "document")

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token),
    path('api-auth/', include('rest_framework.urls')),
]
