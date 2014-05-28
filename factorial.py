#!/usr/bin/env python
# coding: utf-8


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def main():
    try:
        n = int(raw_input('Entre com um número inteiro: '))
        print 'factorial(%i) = %i' % (n, factorial(n))
    except ValueError:
        print 'Somente números inteiros são aceitos!'
        main()

if __name__ == '__main__':
    main()
