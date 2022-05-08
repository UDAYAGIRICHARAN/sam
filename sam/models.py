from django.db import models

class customer(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    income=models.IntegerField()
    assets=models.IntegerField()
    yearsinbussiness=models.IntegerField()
class customer1(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
   
  
# Create your models here.
# Create your models here.
    
    

    
