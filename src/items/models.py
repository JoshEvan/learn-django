from django.db import models
from django.urls import reverse

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places = 2, max_digits=100)

    def get_absolute_url(self):
        return reverse('items:detail', kwargs={'idItem':self.id})

    def get_index_url(self):
        return reverse("items:index")

    def get_update_url(self):
        return reverse('items:update',kwargs={'idItem':self.id})

    def get_delete_url(self):
        return reverse('items:delete',kwargs={'idItem':self.id})