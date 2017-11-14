#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numbers
import time_bz


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


def write(content):
    print content
    # file_name = __file__.split('.')[0] + time_bz.getYearMonthDay()
    file_name = time_bz.getYearMonthDay()
    the_file = open(file_name, 'a')
    the_file.write(content + '\n')


def main():
    type = getType()
    oper = getOper()
    max = getMaxValue()
    if oper == 'buy':
        key = max - type + 0.1
        stop = key - 12

        write('stop at %s, throw at %s' % (stop, stop + 20))
        write('buy 0.1 at %s' % (key + 4))
        write('buy 0.2 at %s' % key)
        write('buy 0.4 at %s' % (key - 4))
        write('buy 0.6 at %s' % (key - 8))
    if oper == 'sell':
        key = max + type - 0.1
        stop = key + 12
        write('stop at %s, throw at %s' % (stop, stop - 20))
        write('sell 0.1 at %s' % (key - 4))
        write('sell 0.2 at %s' % key)
        write('sell 0.4 at %s' % (key + 4))
        write('sell 0.6 at %s' % (key + 8))
if __name__ == '__main__':
    main()
