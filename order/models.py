from django.db import models

# Create your models here.

class Order(models.Model):
    TGId = models.CharField(max_length=255)
    Merch_Id = models.CharField(max_length=255, default=None)
    Branch_Id = models.CharField(max_length=255, default=None)
    Order_id = models.CharField(max_length=255)
    Platform = models.CharField(max_length=255)
    Displayed_id = models.CharField(max_length=255,default=None, blank=True, null=True)
    Price = models.FloatField(default=None, blank=True, null=True)
    Placed_at = models.DateTimeField(blank=True)
    Cart = models.TextField(default=None, blank=True, null=True)
