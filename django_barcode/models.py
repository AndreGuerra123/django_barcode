from django.db import models
from .fields import BarcodeField
class Barcode(models.Model):
    bc = BarcodeField()

class BarcodePK(models.Model):
    bc = BarcodeField(primary_key=True)

class BarcodeUnique(models.Model):
    bc = BarcodeField(unique=True)

class BarcodeCB(models.Model):
    bc = BarcodeField(country='123',brand='1234')

class BarcodeAll(models.Model):
    bc = BarcodeField(primary_key=True,unique=True,country='123',brand='1234')