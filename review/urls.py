from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("home", views.home, name="home"),
]

"add attr home to views.py file"