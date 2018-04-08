from django.urls import path
from . import views

app_name = "Apple"
urlpatterns = [
    path("", views.index, name = "index"),
]
