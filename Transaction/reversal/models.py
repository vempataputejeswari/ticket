from django.db import models

# Create your models here.

class Transaction(models.Model):
	name = models.CharField(max_length=50)
	address = models.CharField(max_length=50)
	bankname = models.CharField(max_length=50)
	transactionid = models.IntegerField()
	phonenumber = models.IntegerField()

	def _str_ (self):
	    return self.name