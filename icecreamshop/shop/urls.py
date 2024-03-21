from django.urls import path
from . import views

app_name = "shop"
urlpatterns = [
    path("", views.index, name="index"),
    path("flavors/", views.FlavorsIndexView.as_view(),name="flavors"),
    path("flavors/<int:pk>/", views.FlavorDetailView.as_view(),name="flavors/detail"),
    path("treats/", views.TreatsIndexView.as_view(),name="treats"),
    path("treats/<int:pk>/", views.TreatDetailView.as_view(),name="treats/detail"),
]
