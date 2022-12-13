from django.db import models


class Color(models.Model):
    color_name = models.CharField(max_length=50)


    def __str__(self):
        return self.color


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    color = models.ForeignKey(Color, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


