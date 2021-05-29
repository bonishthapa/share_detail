from django.db import models

# Create your models here.


class ShareBrought(models.Model):
    name = models.CharField(max_length=150, blank=True)
    quantity = models.IntegerField()
    brought_rate = models.IntegerField()
    brought_date = models.DateField()

    @property
    def total_price(self):
        return self.quantity * self.brought_rate

    def __str__(self):
        return self.name

class ShareSold(models.Model):
    name = models.CharField(max_length=150, blank=True)
    quantity = models.IntegerField()
    brought_rate = models.IntegerField()
    brought_date = models.DateField()
    sold_rate = models.IntegerField()
    sold_date = models.DateField()
    

    @property
    def brought_total_price(self):
        return self.quantity * self.brought_rate

    @property
    def sold_total_price(self):
        return self.quantity * self.sold_rate    

    @property
    def profit_or_loss(self):
        return self.sold_total_price - self.brought_total_price

    def __str__(self):
        return self.name    