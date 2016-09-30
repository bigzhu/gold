#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
卖出：10日内最高-浮动(FLUC)
止盈(T/P): + 2*ATR
止损(S/L): + UNIT + ATR + (ATR / 2)
救卖出: +(ATR/2)
追加: - UNIT 4-5 个


'''
import sys
import ConfigParser
config = ConfigParser.ConfigParser()
with open('config.ini', 'r') as cfg_file:
    config.readfp(cfg_file)
    ATR = float(config.get('config', 'ATR'))
    LONG_DAY = int(config.get('config', 'LONG_DAY'))
    SHORT_DAY = int(config.get('config', 'SHORT_DAY'))
    SELL_SAVE_AT = float(config.get('config', 'SELL_SAVE_AT'))
    SELL_AT = float(config.get('config', 'SELL_AT'))
    SELL_AT1 = float(config.get('config', 'SELL_AT1'))
    SELL_AT2 = float(config.get('config', 'SELL_AT2'))
    SELL_AT3 = float(config.get('config', 'SELL_AT3'))
    SELL_AT4 = float(config.get('config', 'SELL_AT4'))

UNIT = (ATR / 10)
FLUC = (ATR / 4)  # 购买浮动
print 'UNIT=%.3f' % UNIT


def readGodDatas(day_count):
    high = []
    low = []
    f = open(sys.path[0] + '/XAUUSD', 'r')
    for i in f:
        god_data = i.split('|')
        high.append(float(god_data[0]))
        low.append(float(god_data[1]))
        if len(low) == int(day_count):
            break
    f.close()
    return high, low

high, low = readGodDatas(LONG_DAY)
L_HIGH = max(high)
L_LOW = min(low)
high, low = readGodDatas(SHORT_DAY)
S_HIGH = max(high)
S_LOW = min(low)


def getSellAt():
    '''
    卖出：10日内最高-浮动(FLUC)
    '''
    sell_at = L_HIGH - FLUC
    return sell_at


def getSellTP(sell_at):
    '''
    止盈(T/P): 2*ATR
    '''
    return sell_at - (2 * ATR)


def getSellSave(sell_at):
    '''
    救卖出: +(ATR/2)
    '''
    return sell_at + (ATR / 2)


def getSellSL(sell_at):
    '''
    止损(S/L): + UNIT + ATR + (ATR / 2)
    '''
    return sell_at + UNIT + ATR + (ATR / 2)


def appendSell(last_sell_at):
    '''
    追加: - UNIT 4-5 个
    '''
    sell = last_sell_at - UNIT
    return sell


def printSell(name, sell_at):
    print "%s=%.3f S/L=%.3f T/P=%.3f" % (name, sell_at, getSellSL(sell_at), getSellTP(sell_at))


def sell():
    sell_at = getSellAt()
    if SELL_AT != 0:  # 买了
        sell_at = SELL_AT
    else:
        sell_at = getSellAt()
    if SELL_SAVE_AT != 0:  # 买了抄底
        sell_at_save = SELL_SAVE_AT
    else:
        sell_at_save = getSellSave(sell_at)
    printSell('sell_at_save', sell_at_save)
    printSell('sell_at', sell_at)
    if SELL_AT1 != 0:
        sell_at1 = SELL_AT1
    else:
        sell_at1 = appendSell(sell_at)
    printSell('sell_at1', sell_at1)

    if SELL_AT2 != 0:
        sell_at2 = SELL_AT2
    else:
        sell_at2 = appendSell(sell_at1)
    printSell('sell_at2', sell_at2)

    if SELL_AT3 != 0:
        sell_at3 = SELL_AT3
    else:
        sell_at3 = appendSell(sell_at2)
    printSell('sell_at3', sell_at3)

    if SELL_AT4 != 0:
        sell_at4 = SELL_AT4
    else:
        sell_at4 = appendSell(sell_at3)
    printSell('sell_at4', sell_at4)


def getBuy():
    buy = L_LOW + FLUC
    buy_stop = L_LOW - ATR
    # print "buy_-1=%.3f buy__stop-1=%.3f" % (buy - (ATR / 2), buy_stop - (ATR / 2))
    print "buy0=%.3f buy_stop0=%.3f" % (buy, buy_stop)
    # buy = appendBuy(buy, UNIT, 1)
    # buy = appendBuy(buy, UNIT, 2)
    # buy = appendBuy(buy, UNIT, 3)


def appendBuy(value, UNIT, count):
    buy = value + UNIT
    buy_stop = buy - ATR
    print "buy_%s=%.3f buy__stop%s=%.3f" % (count, buy, count, buy_stop)
    return buy


def main():
    sell()
    print ''
    getBuy()

if __name__ == '__main__':
    main()
