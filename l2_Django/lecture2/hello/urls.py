from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("yubo", views.yubo, name="yubo"),
    path("<str:name>", views.greet, name="greet")
]