from django.test import TestCase
from .models import Customer

class CustomerTestCase(TestCase):
    def test_customer_setup_and_teardown(self):
        """Model can be created and deleted?"""
        new_customer = Customer.objects.create(first_name="John", last_name="Smith", address="1234 Address Road", city="Denver", state="CO", zip="80014")
        self.assertIsNotNone(new_customer.id)
        Customer.objects.filter(id=new_customer.id).delete()
        self.assertEqual(len(Customer.objects.filter(id=new_customer.id)), 0)
