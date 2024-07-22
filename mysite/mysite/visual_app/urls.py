from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("get_aggregate/", views.get_aggregate, name="about"),
    path("get_exact/", views.get_exact, name="about"),
]