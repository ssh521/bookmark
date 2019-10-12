from django.db import models
from django.urls import reverse

class Bookmark (models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    def __str__(self):
        #객체를 출력할 때 나타날 값
        return  self.site_name + " " + self.url

    def get_absolute_url(self):
        return reverse('detail', args=[self.id])

