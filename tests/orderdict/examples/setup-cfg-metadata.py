#!/usr/bin/env python
import orderdict

metadata = dict(version="1.0.0", name="pkgname")
print(metadata)
print(orderdict.order(["name", "version"], metadata))
