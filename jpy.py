#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gold import getType, getOper, getMaxValue

if __name__ == '__main__':

    type = getType()
    oper = getOper()
    max = getMaxValue()
    if oper == 'buy':
        key = max - type / 10.00 + 0.01
        stop = key - 1
        print('buy 0.2 at %s, %s' % (key, stop))
        print('buy 0.4 at %s, %s' % (key - 0.2, stop))
        print('buy 0.6 at %s, %s' % (key - 0.6, stop))
    if oper == 'sell':
        key = max + type / 10.00 - 0.01
        stop = key + 1
        print('sell 0.2 at %s, %s' % (key, stop))
        print('sell 0.4 at %s, %s' % (key + 0.2, stop))
        print('sell 0.6 at %s, %s' % (key + 0.6, stop))
