#!/usr/bin/env python
# -*- coding: utf-8 -*-
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
top = int(float(config.get('gold', 'top')) * 1000)


def getOper():
    '''
    取类型
    '''
    oper = input("buy or sell: ")
    if oper not in ['buy', 'sell']:
        print('请输入buy sell 之一!')
        return getOper()
    return oper


def getAtr():
    atr = input("当天12点 ATR:")
    try:
        atr = int(float(atr) * 1000)
    except ValueError:
        print('请输入正确的数字!')
        return getAtr()
    return atr


def getTop():
    top = input("近4天峰值:")
    try:
        top = int(float(top) * 1000)
    except ValueError:
        print('请输入正确的数字!')
        return getTop()
    return top


def main():
    oper = getOper()
    atr = getAtr()
    # top = getTop()
    print('近4天峰值: %s' % (top / 1000))
    one_quarter = atr / 4
    print('购买间隔: %s' % (one_quarter / 1000))

    two_atr = 2 * atr
    if oper == 'buy':
        reverse = top - two_atr
    else:
        reverse = top + two_atr
    print('保底: %s' % (reverse / 1000))
    print('-------------------------------------------------------')
    tmp = top
    for i in range(1, 14):
        if oper == 'buy':
            tmp = tmp - one_quarter
        else:
            tmp = tmp + one_quarter
        print(tmp / 1000)


if __name__ == '__main__':
    main()
    #import doctest
    #doctest.testmod(verbose=False, optionflags=doctest.ELLIPSIS)
