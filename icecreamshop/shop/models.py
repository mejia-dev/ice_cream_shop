from django.db import models

class Flavor(models.Model):
    flavor_name = models.CharField(max_length=100)
    price = models.IntegerField(default=1)

    def __str__(self):
        return self.flavor_name
    

class Treat(models.Model):
    treat_name = models.CharField(max_length=100)
    price = models.IntegerField(default=5)
    flavors = models.ManyToManyField(Flavor)

    def __str__(self):
        return self.treat_name