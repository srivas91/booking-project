from django.db import models
from django.contrib import admin

# Create your models here.

class Customer(models.Model):
    cusid=models.IntegerField(primary_key=True)
    cusname=models.CharField(max_length=30)
    mobnum=models.CharField(max_length=10)
    emailid=models.EmailField(max_length=50)

    def __str__(self):
        return f'{self.cusid}-{self.cusname}-{self.mobnum}-{self.emailid}'

class Booking(models.Model):
    bookid=models.IntegerField(primary_key=True)
    mysource = [('chennai', 'chennai'), ('trichy', 'trichy')]
    source = models.CharField(choices=mysource,default='chennai',max_length=30)
    mydestination = [('trichy', 'trichy'), ('madurai', 'madurai')]
    destination = models.CharField(choices=mydestination,default='trichy',max_length=30)
    mychoice=[('sleeper','sleeper'),('general','general')]
    type=models.CharField(choices=mychoice,max_length=30,default='general')
    seatnum=models.IntegerField()
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    bookdate=models.DateTimeField()

class CustomerAdmin(admin.ModelAdmin):
    models='Customer'
    list_display =['cusid','cusname','mobnum','emailid']

class BookingAdmin(admin.ModelAdmin):
    models='Customer'
    list_display =['bookid','seatnum','bookdate']
