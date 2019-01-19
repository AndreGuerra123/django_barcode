from django.db import models
from .fields import BarcodeField

class Barcode(models.Model):
    bc = BarcodeField()
