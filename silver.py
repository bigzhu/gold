#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gold
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
top = int(float(config.get('silver', 'top')) * 1000)

gold.top = top


def main():
    gold.main()


if __name__ == '__main__':
    main()
    #import doctest
    #doctest.testmod(verbose=False, optionflags=doctest.ELLIPSIS)
