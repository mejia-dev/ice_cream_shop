from django.urls import path
from . import views

app_name = "shop"
urlpatterns = [
    path("", views.index, name="index"),
    path("flavors/", views.FlavorsIndexView.as_view(),name="flavors")
]
