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
    SELL_AT = float(config.get('config', 'SELL_AT'))
    SELL_AT1 = float(config.get('config', 'SELL_AT1'))


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


def getSell(high, low):
    unit = (ATR / 10)

    sell = high - unit
    sl = high + ATR
    if SELL_AT != 0:  # 买了
        if SELL_AT1 != 0:  # 买了追加
            sell_at1_sl = SELL_AT + unit + ATR + (ATR / 2)
            sell_at1_tp = low + ATR
            print "sell_at(1)=%.3f S/L=%.3f T/P=%.3f" % (SELL_AT1, sell_at1_sl, sell_at1_tp)
        else: # 没追加
            sell1 = SELL_AT + (ATR / 2)
            sell1_sl = sell1 + unit + ATR + (ATR / 2)
            sell1_tp = low + ATR
            print "sell(1)=%.3f S/L=%.3f T/P=%.3f" % (sell1, sell1_sl, sell1_tp)

        sell_at_sl = SELL_AT + unit + ATR
        sell_at_tp = low + (ATR / 2)
        print "sell_at=%.3f S/L=%.3f T/P=%.3f" % (SELL_AT, sell_at_sl, sell_at_tp)
        if SELL_AT1 == 0:  # 没有买2保时再追加
            sell = appendSell(SELL_AT, unit, 1)
            sell = appendSell(sell, unit, 2)
            sell = appendSell(sell, unit, 3)
    else:
        print "sell0=%.3f S/L=%.3f" % (sell, sl)

    # sell = appendSell(sell, unit, 1)
    # sell = appendSell(sell, unit, 2)
    # sell = appendSell(sell, unit, 3)


def appendSell(value, unit, count):
    sell = value - unit
    sl = value + ATR
    print "sell%s=%.3f S/L%s=%.3f" % (count, sell, count, sl)
    return sell


def getBuy(low):
    unit = (ATR / 10)
    buy = low + unit
    buy_stop = low - ATR
    # print "buy_-1=%.3f buy__stop-1=%.3f" % (buy - (ATR / 2), buy_stop - (ATR / 2))
    print "buy_0=%.3f buy__stop0=%.3f" % (buy, buy_stop)
    # buy = appendBuy(buy, unit, 1)
    # buy = appendBuy(buy, unit, 2)
    # buy = appendBuy(buy, unit, 3)


def appendBuy(value, unit, count):
    buy = value + unit
    buy_stop = buy - ATR
    print "buy_%s=%.3f buy__stop%s=%.3f" % (count, buy, count, buy_stop)
    return buy


def main():
    high, low = readGodDatas()
    high = max(high)
    low = min(low)
    getSell(high, low)
    print ''
    print ''
    getBuy(low)

if __name__ == '__main__':
    main()
