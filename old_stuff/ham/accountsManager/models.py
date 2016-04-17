from django.db import models
from decimal import *
from django import forms
from django.forms import ModelForm
#from django import ModelForm


# Create your models here.

class Account(models.Model):
	name = models.CharField(max_length=200)
	balance = models.DecimalField(max_digits=5, decimal_places=2)
	
	def __unicode__(self):
			return self.name
			
	def get_balance(self):
			return str(self.balance)
			
	def process_transaction(self, transaction):
			self.balance +=transaction.amount
			return str(self.balance)
	

class Transaction(models.Model):
	name = models.CharField(max_length=200)
	amount = models.DecimalField(max_digits=5, decimal_places=2)
	account = models.ForeignKey('Account')
	
	def __unicode__(self):
			return self.name
			
			

class TransactionForm(ModelForm):
	class Meta:
		model = Transaction
