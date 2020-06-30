<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/orderdict.svg?maxAge=3600)](https://pypi.org/project/orderdict/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/orderdict.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/orderdict.py/actions)

### Installation
```bash
$ [sudo] pip install orderdict
```

#### Examples
```python
>>> import orderdict

>>> metadata = dict(version="1.0.0", name="pkgname")
{'version': '1.0.0', 'name': 'pkgname'}

>>> orderdict.order(["name", "version"], metadata)
OrderedDict([('name', 'pkgname'), ('version', '1.0.0')])
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>