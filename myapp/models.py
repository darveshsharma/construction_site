from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.EmailField(max_length=100)
    contact=models.CharField(max_length=12)
    desc=models.TextField(max_length=200)
    date=models.DateField()
    
    def __str__(self):
        return self.name
    