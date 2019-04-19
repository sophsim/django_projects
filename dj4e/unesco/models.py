from django.db import models

class Category(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class Iso(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class States(models.Model) :
    states = models.CharField(max_length=128)
    justification = models.CharField(max_length=500)
    description = models.CharField(max_length=500)

    def __str__(self) :
        return self.states

class Region(models.Model) :
    latitude = models.IntegerField(null=True)
    longitude = models.IntegerField(null=True)
    area_hectares = models.IntegerField(null=True)

    def __str__(self) :
        return self.region

class Site(models.Model):
    name = models.CharField(max_length=128)
    year = models.IntegerField(null=True)
    iso = models.ForeignKey(Iso, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    region = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) :
        return self.name
