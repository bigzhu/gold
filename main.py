#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import ConfigParser
config = ConfigParser.ConfigParser()
with open('config.ini', 'r') as cfg_file:
    config.readfp(cfg_file)
    ATR = float(config.get('config', 'ATR'))
    LONG_DAY = int(config.get('config', 'LONG_DAY'))
    SHORT_DAY = int(config.get('config', 'SHORT_DAY'))


def readGodDatas():
    high = []
    low = []
    f = open(sys.path[0] + '/XAUUSD', 'r')
    for i in f:
        god_data = i.split('|')
        high.append(float(god_data[0]))
        low.append(float(god_data[1]))
        if len(low) == int(LONG_DAY):  # 不取多过 LONG_DAY 的数
            break
    f.close()
    return high, low


def getSell(high):
    max_high = max(high)
    unit = (ATR / 10)

    sell = max_high - unit
    sell_stop = sell + ATR
    print "sell0=%.3f sell_stop0=%.3f" % (sell, sell_stop)
    sell = appendSell(sell, unit, 1)
    sell = appendSell(sell, unit, 2)
    sell = appendSell(sell, unit, 3)


def appendSell(value, unit, count):
    sell = value - unit
    sell_stop = sell + ATR
    print "sell%s=%.3f sell_stop%s=%.3f" % (count, sell, count, sell_stop)
    return sell


def getBuy(low):
    min_low = min(low)
    unit = (ATR / 10)
    buy = min_low + unit
    buy_stop = buy - ATR
    print "buy_0=%.3f buy__stop0=%.3f" % (buy, buy_stop)
    buy = appendBuy(buy, unit, 1)
    buy = appendBuy(buy, unit, 2)
    buy = appendBuy(buy, unit, 3)


def appendBuy(value, unit, count):
    buy = value + unit
    buy_stop = buy - ATR
    print "buy_%s=%.3f buy__stop%s=%.3f" % (count, buy, count, buy_stop)
    return buy


def main():
    high, low = readGodDatas()
    getSell(high)
    print ''
    print ''
    getBuy(low)

if __name__ == '__main__':
    main()
