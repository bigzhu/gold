#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numbers


def getType():
    '''
    取趋势
    '''
    type = input("趋势6, 半趋势4, 无2, 逆半趋势0, 逆趋势-2: ")
    if type not in [6, 4, 2, 0, -2]:
        print('请输入6 4 2 0 -2 之一!')
        return getType()
    return type


def getOper():
    '''
    取类型
    '''
    oper = raw_input("buy or sell: ")
    if oper not in ['buy', 'sell']:
        print('请输入buy sell 之一!')
        return getOper()
    return oper


def getMaxValue():
    '''
    '''
    max = input("max: ")
    if not isinstance(max, numbers.Real):
        print('请输入正确的数字!')
        return getMaxValue()
    return max
if __name__ == '__main__':
    type = getType()
    oper = getOper()
    max = getMaxValue()
    if oper == 'buy':
        key = max - type + 0.1
        stop = key - 10
        print('buy 0.2 at %s, %s' % (key, stop))
        print('buy 0.4 at %s, %s' % (key - 2, stop))
        print('buy 0.6 at %s, %s' % (key - 6, stop))
    if oper == 'sell':
        key = max + type - 0.1
        stop = key + 10
        print('sell 0.2 at %s, %s' % (key, stop))
        print('sell 0.4 at %s, %s' % (key + 2, stop))
        print('sell 0.6 at %s, %s' % (key + 6, stop))
