from django.db import models

class Medicine(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    price=models.TextField()


    def __str__(self):
        return self.name
    

class Doctors(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()


