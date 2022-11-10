from django.test import TestCase

# Create your tests here.

# Create your tests here.
from reversal.models import Transaction

class MyTest(TestCase):
	def test_record(self):
		try:
			obj = product(name="teju",
			   details= "i want my money back", transactionid= 8,
			   phonenumber= 9963923186)
			obj.save()
			self.assertEquals(obj.transactionid,8,"transactionid mismatch")
			self.assertEquals(obj.phonenumber,9963923186,"number mismatch")
			
		except Exception as e:
			print('unable to insert request response')
