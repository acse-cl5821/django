from django.db import models

# Create your models here.

class Order(models.Model):
    TGId = models.CharField(max_length=255)
    Order_id = models.CharField(max_length=255)
    Platform = models.CharField(max_length=255)
    Displayed_id = models.CharField(max_length=255,blank=True)
    Current_state = models.CharField(max_length=255,blank=True)
    Cart = models.TextField()
    Store_id = models.IntegerField()
    Placed_at = models.DateTimeField(blank=True)
