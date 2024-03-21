from django.shortcuts import render
from django.views import generic

from .models import Flavor, Treat

def index(request):
    return render(request, "shop/index.html",)

class FlavorsIndexView(generic.ListView):
    template_name = "shop/flavors/index.html"
    context_object_name = "flavors_list"

    def get_queryset(self):
        return Flavor.objects.order_by("flavor_name")
    
class TreatsIndexView(generic.ListView):
    template_name = "shop/treats/index.html"
    context_object_name = "treats_list"

    def get_queryset(self):
        return Treat.objects.order_by("treat_name")