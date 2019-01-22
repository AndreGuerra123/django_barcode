
[![Build Status](https://travis-ci.org/AndreGuerra123/django_barcode.png)](https://travis-ci.org/AndreGuerra123/django_barcode)
[![codecov](https://codecov.io/gh/AndreGuerra123/django_barcode/branch/master/graph/badge.svg)](https://codecov.io/gh/AndreGuerra123/django_barcode)

# Django Barcode

Django Barcode is a Django (Python) library with a [EAN-13](https://en.wikipedia.org/wiki/International_Article_Number) standard barcode field. 
It provides the means of supplying to Django models the capability of storing a standarized barcode.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Django Barcode.

```bash

pip install django_barcode

```

## Usage

Just add the field to your models. No need to modify settings file.

```python

from django.db import models 
from django_barcode.fields import BarcodeField

class Product(models.Model):
    bc = BarcodeField()

```

Alternatively, it can be used as the foreign key:

```python

from django.db import models 
from django_barcode.fields import BarcodeField

class Product(models.Model):
    id = BarcodeField(unique=True)

```

The default values for the Country and Brand specification on the barcode are '950' and '0000'.
The Country and Brand specification on the barcode may be altered in one of 2 ways:

- Changing global defaults on settings.py file:
```python

BARCODE_COUNTRY = '123' 
BARCODE_BRAND = '1234'

```

- Change field-specific defaults by setting the *kwargs explicitly:
```python

class Product(models.Model):
    id = BarcodeField(unique=, country='123',brand='1234')


```

The Barcode Field as a current limitation set by the EAN standard of  100 000 unique elements.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)