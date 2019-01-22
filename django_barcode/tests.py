from django.test import TestCase
from .models import Barcode, BarcodePK, BarcodeUnique, BarcodeCB, BarcodeAll

class BarcodeTestCase(TestCase):
    def setUp(self):
        Barcode.objects.create()
        BarcodePK.objects.create()
        BarcodeUnique.objects.create()
        BarcodeCB.objects.create()
        BarcodeAll.objects.create()
        
    def test_barcode(self):
        """ Test simple barcode creation """
        bc = Barcode.objects.all().first()
        bcpk = BarcodePK.objects.all().first()
        bcu = BarcodeUnique.objects.all().first()
        bccb = BarcodeCB.objects.all().first()
        bcall = BarcodeAll.objects.all().first()

        self.assertEqual(bc!=None,True)
        self.assertEqual(bcpk!=None,True)
        self.assertEqual(bcu!=None,True)
        self.assertEqual(bccb!=None,True)
        self.assertEqual(bcall!=None,True)
