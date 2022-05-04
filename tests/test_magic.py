#!/usr/bin/env python
# -*- coding: utf-8 -*-
from magic import Magic


def test_magic():
    source = "UB12345678901"
    magic = Magic(source=source)
    result = magic.convert2Int()
    assert result == 781038213
