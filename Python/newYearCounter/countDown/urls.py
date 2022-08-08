from . import views

from django.urls import path

# this list contains the url and their corresponding views to render.

urlpatterns = [
    path("", views.index, name="index")
]