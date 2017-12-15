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


def trade(oper, top, atr):
    '''
    计算购入点
    >>> trade('buy', 1296940, 9800)
    {'reverse': 1277.34, 'intervals': [1294.49, 1292.04, 1289.59, 1287.14, 1284.69, 1282.24, 1279.79, 1277.34, 1274.89, 1272.44, 1269.99, 1267.54, 1265.09]}
    '''
    two_atr = 2 * atr
    one_quarter = atr / 4
    if oper == 'buy':
        reverse = top - two_atr
    else:
        reverse = top + two_atr
    result = dict(reverse=reverse / 1000)
    intervals = []
    tmp = top
    for i in range(1, 14):
        if oper == 'buy':
            tmp = tmp - one_quarter
        else:
            tmp = tmp + one_quarter
        intervals.append(tmp / 1000)
    result['intervals'] = intervals
    return result


def main():
    '''
    '''
    oper = getOper()
    atr = getAtr()
    # top = getTop()
    print('近4天峰值: %s' % (top / 1000))
    one_quarter = atr / 4
    print('购买间隔: %s' % (one_quarter / 1000))
    result = trade(oper, top, atr)
    result_str = '''保底: %s'
-------------------------------------------
''' % result['reverse']
    for i in result['intervals']:
        result_str += str(i) + '\n'
    print(result_str)


if __name__ == '__main__':
    main()
    # import doctest
    # doctest.testmod(verbose=False, optionflags=doctest.ELLIPSIS)
