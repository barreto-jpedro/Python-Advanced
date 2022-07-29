from datetime import datetime as dt

from django.db import models

# Create your models here.


class DjangoProject(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    modules_numbers = models.DecimalField(decimal_places=2, max_digits=1000)
    date = models.DateTimeField("Published in ", default=dt.now())

    def __str__(self):
        return self.title
