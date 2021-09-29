from django.db import models

# Create your models here.
class Coin(models.Model):
    name=models.CharField(max_length=100)

class Blog(models.Model):
    category=models.ForeignKey(Coin,on_delete=models.CASCADE,default=None)
    title=models.CharField(max_length=60)
    image=models.ImageField(upload_to='images')
    desc=models.CharField(max_length=150)
    body=models.TextField(max_length=4000,default='Nothin')
    time=models.DateTimeField(auto_now_add=True)

class Buy_Sell(models.Model):
    title=models.CharField(max_length=60)
    image=models.ImageField(upload_to='images')
    desc=models.CharField(max_length=150)
    body=models.TextField(max_length=4000,default='Nothin')
    time=models.DateTimeField(auto_now_add=True)

class Mining(models.Model):
    title=models.CharField(max_length=60)
    image=models.ImageField(upload_to='images')
    desc=models.CharField(max_length=150)
    body=models.TextField(max_length=4000,default='Nothin')
    time=models.DateTimeField(auto_now_add=True)


class Pricing(models.Model):
    title=models.CharField(max_length=60)
    image=models.ImageField(upload_to='images')
    desc=models.CharField(max_length=150)
    body=models.TextField(max_length=4000,default='Nothin')
    time=models.DateTimeField(auto_now_add=True)


class Blochchain(models.Model):
    title=models.CharField(max_length=60)
    image=models.ImageField(upload_to='images')
    desc=models.CharField(max_length=150)
    body=models.TextField(max_length=4000,default='Nothin')
    time=models.DateTimeField(auto_now_add=True)

class Guide(models.Model):
    title=models.CharField(max_length=60)
    image=models.ImageField(upload_to='images')
    desc=models.CharField(max_length=150)
    body=models.TextField(max_length=4000,default='Nothin')
    time=models.DateTimeField(auto_now_add=True)

class Messages(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    subject=models.CharField(max_length=100)
    message=models.CharField(max_length=1000)



