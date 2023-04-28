from django.db import models
from django.urls import reverse


class Data(models.Model):
    data = models.TextField()

    def get_absolute_url(self):
        return reverse('idpage', kwargs={'data_id': self.pk})
