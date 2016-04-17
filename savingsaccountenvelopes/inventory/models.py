from django.db import models

# Create your models here.


class Item(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	amount = models.IntegerField()

class Account(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	currentBalance = models.IntegerField()

class Transaction(models.Model):
	description = models.TextField()
	amount = models.IntegerField()
# how to i create an attribute with is another object. 
#the field should populate by only one of the existing instances of Account
#	account = this.Account()





