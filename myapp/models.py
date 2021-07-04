from django.db import models



class Point(models.Model):
    lon = models.BigIntegerField(default=0)
    lat = models.BigIntegerField(default=0)


class Areas(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    points = models.OneToOneField(Point, on_delete=models.CASCADE, null=True)
    fill_type = models.CharField(max_length=20)
    color1 = models.CharField(max_length=20)
    color2 = models.CharField(max_length=20)
    angle = models.IntegerField(null = True)

    def __str__(self):
        return self.name
