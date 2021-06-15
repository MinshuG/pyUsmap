# pyUsmap
.usmap reader

[![pypi](https://img.shields.io/pypi/v/valorant-api.svg)](https://pypi.python.org/pypi/valorant-api/)
[![Downloads](https://pepy.tech/badge/pyusmap)](https://pepy.tech/project/pyusmap)

# Installation
`pip install pyUsmap`

# Usages
```py
from Usmap import Usmap
import json

with open("xyz.usmap", "rb") as f:
    data = Usmap(f).read()

# from bytes or byte array
import io

data = Usmap(io.BytesIO(b'')).read()

# writing to json
jsondict = data.GetValue() # get json serializable dict
with open("Mappings.json", "w") as f:
    json.dump(jsondict, f, indent=4)


```
# Requirements

* Python 3
* Brotli