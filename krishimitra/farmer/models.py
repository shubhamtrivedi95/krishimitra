from django.db import models

# Create your models here.
class client(models.Model):

    MobileNo = models.IntegerField()
    CustmerName=models.CharField(max_length=20)
    Enable = models.IntegerField(null=True, blank=True)
    DeviceId=models.IntegerField(unique=True)
    AmtOfWater=models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.CustmerName