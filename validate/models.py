from django.db import models

# Create your models here.
class Validate(models.Model):
    MerchID = models.CharField(max_length=255)
    BranchID = models.CharField(max_length=255)
    ValidUntil = models.DateField()
    HungryPanda = models.BooleanField()
    HP_Valid = models.DateField(default=None, blank=True, null=True)
    Deliveroo = models.BooleanField()
    DR_Valid = models.DateField(default=None, blank=True, null=True)
    UberEats = models.BooleanField()
    UE_Valid = models.DateField(default=None, blank=True, null=True)
    Fantuan = models.BooleanField()
    FT_Valid = models.DateField(default=None, blank=True, null=True)

