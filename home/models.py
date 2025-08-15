from django.db import models

# Create your models here.
#table for storing the data form contact us page
class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    email=models.CharField(max_length=50)
    content=models.TextField()
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)


    def __str__(self):
        return 'Message from '+self.name + ' - ' + self.email