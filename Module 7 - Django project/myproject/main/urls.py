from django.urls import path

from . import views

app_main = "main"

urlpatterns = [
    path("", views.homepage, name="homepage"),
]
