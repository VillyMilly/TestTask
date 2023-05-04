from django.db import models


class Data(models.Model):
    data = models.TextField()

    def __str__(self):
        return self.data
