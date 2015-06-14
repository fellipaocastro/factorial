#!/usr/bin/env python
# coding: utf-8
from __future__ import absolute_import

from factorial import factorial


def main():
    try:
        number = int(raw_input('Entre com um número inteiro: '))
        print 'factorial({0}) = {1}'.format(number, factorial(number))
    except ValueError:
        print 'Somente números inteiros são aceitos!'
        main()

if __name__ == '__main__':
    main()
