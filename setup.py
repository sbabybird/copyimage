#!/usr/bin/env python
# -*- coding:gbk -*-

from distutils.core import setup
import py2exe
setup(console=[{"script" : "copyimage.py"}], options={"py2exe" : {"includes" : ["os", "sys", "PIL.Image"]}})
