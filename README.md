# pyUsmap
.usmap parser

# Installation
`pip install pyUsmap`

# Usages
```py
from Usmap import Usmap

with open("xyz.usmap", "rb") as f:
    data = Usmap(f).read()

# from bytes or byte array
import io

data = Usmap(io.BytesIO(b'')).read()

```
# Requirements

* Python 3
* Brotli