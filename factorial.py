#!/usr/bin/env python
# coding: utf-8


def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)


def main():
    try:
        number = int(raw_input('Entre com um número inteiro: '))
        print 'factorial(%i) = %i' % (number, factorial(number))
    except ValueError:
        print 'Somente números inteiros são aceitos!'
        main()

if __name__ == '__main__':
    main()
