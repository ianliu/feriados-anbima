#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(name='feriados-anbima',
      version='0.1.0',
      py_modules=['anbima'],
      author='Ian Liu Rodrigues',
      author_email='ian.liu88@gmail.com',
      description='Facilita o uso do módulo "bizdays"',
      url='https://github.com/ianliu/feriados-anbima',
      license='GPL3',
      keywords='feriados, anbima, bizdays, dias úteis',
      long_description='''Exemplo de uso:
    >>> from bizdays import Calendar
    >>> from anbima import holidays
    cal = Calendar(holidays(), ['Saturday', 'Sunday'])
    ''')
