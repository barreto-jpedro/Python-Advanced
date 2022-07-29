from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path("", include("main.urls")),
    path("admin/", admin.site.urls),
]
