from django.db import models

# Create your models here.
class client(models.Model):

    MobileNo = models.IntegerField(unique=True)
    CustmerName=models.CharField(max_length=20)
    Enable = models.IntegerField(null=True, blank=True)
    DeviceId=models.IntegerField(unique=True)
    AmtOfWater=models.IntegerField(null=True, blank=True)
    Status=models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return "[{},{}]".format(self.CustmerName,self.Enable)