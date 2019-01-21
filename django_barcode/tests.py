from django.test import TestCase
from .models import Barcode

class BarcodeTestCase(TestCase):
    def setUp(self):
        Barcode.objects.create()
        
    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        bc = Barcode.objects.all().first()
        self.assertEqual(bc!=None,True)
