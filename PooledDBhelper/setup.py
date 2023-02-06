# -*- encoding: utf-8 -*-
"""
@Author  : cy1
@File    : setup.py
@Time    : 2023/1/28 14:40
@Software: PyCharm
"""

import setuptools
with open("README.rst",'r',encoding="utf-8")as  fh:
    long_desc=fh.read()
setuptools.setup(
    name='PooledDBhelper',
    version='1.0.0',
    keywords='PooledDBhelper',
    description="A database tool",
    long_description=long_desc,
    long_description_content_type='text/x-rst',
    author="Cyprus0126",
    author_email='2459231463@qq.com',
    url='',
    packages=setuptools.find_packages(),
    license="MIT",
    install_requires=[
            'pymysql','dbutils'
    ]
)