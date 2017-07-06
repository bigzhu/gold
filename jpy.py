#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gold import getType, getOper, getMaxValue, write

if __name__ == '__main__':

    type = getType()
    oper = getOper()
    max = getMaxValue()
    if oper == 'buy':
        key = max - type / 10.00 + 0.01
        stop = key - 1.2
        write('stop at %s, throw at %s' % (stop, stop + 2))
        write('buy 0.2 at %s' % (key))
        write('buy 0.4 at %s' % (key - 0.4))
        write('buy 0.6 at %s' % (key - 0.8))
    if oper == 'sell':
        key = max + type / 10.00 - 0.01
        stop = key + 1.2
        write('stop at %s, throw at %s' % (stop, stop - 2))
        write('sell 0.2 at %s' % (key))
        write('sell 0.4 at %s' % (key + 0.4))
        write('sell 0.6 at %s' % (key + 0.8))
