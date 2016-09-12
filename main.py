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

UNIT = (ATR / 10)


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


def getSellTp(sell_at):
    return sell_at - UNIT - ATR - (ATR / 2)


def getSell(high, low):

    sell = high - UNIT
    sl = high + ATR
    if SELL_AT != 0:  # 买了
        if SELL_AT1 != 0:  # 买了追加
            sell_at1_sl = SELL_AT + UNIT + ATR + (ATR / 2)
            sell_at1_tp = getSellTp(SELL_AT1)
            print "sell_at(1)=%.3f S/L=%.3f T/P=%.3f" % (SELL_AT1, sell_at1_sl, sell_at1_tp)
            sell = appendSell(SELL_AT1, UNIT, 1)
            sell = appendSell(sell, UNIT, 2)
            sell = appendSell(sell, UNIT, 3)
        else:  # 没追加
            sell1 = SELL_AT + (ATR / 2)
            sell1_sl = sell1 + UNIT + ATR + (ATR / 2)
            sell1_tp = getSellTp(sell1)
            print "sell(1)=%.3f S/L=%.3f T/P=%.3f" % (sell1, sell1_sl, sell1_tp)

        sell_at_sl = SELL_AT + UNIT + ATR
        sell_at_tp = getSellTp(SELL_AT)
        print "sell_at=%.3f S/L=%.3f T/P=%.3f" % (SELL_AT, sell_at_sl, sell_at_tp)
        if SELL_AT1 == 0:  # 没有买2保时再追加
            sell = appendSell(SELL_AT, UNIT, 1)
            sell = appendSell(sell, UNIT, 2)
            sell = appendSell(sell, UNIT, 3)
    else:
        print "sell0=%.3f S/L=%.3f" % (sell, sl)

    # sell = appendSell(sell, UNIT, 1)
    # sell = appendSell(sell, UNIT, 2)
    # sell = appendSell(sell, UNIT, 3)


def appendSell(value, UNIT, count):
    sell = value - UNIT
    sl = value + ATR
    tp = getSellTp(sell)

    print "sell%s=%.3f S/L%s=%.3f T/P=%.3f" % (count, sell, count, sl, tp)
    return sell


def getBuy(low):
    UNIT = (ATR / 10)
    buy = low + UNIT
    buy_stop = low - ATR
    # print "buy_-1=%.3f buy__stop-1=%.3f" % (buy - (ATR / 2), buy_stop - (ATR / 2))
    print "buy_0=%.3f buy__stop0=%.3f" % (buy, buy_stop)
    # buy = appendBuy(buy, UNIT, 1)
    # buy = appendBuy(buy, UNIT, 2)
    # buy = appendBuy(buy, UNIT, 3)


def appendBuy(value, UNIT, count):
    buy = value + UNIT
    buy_stop = buy - ATR
    print "buy_%s=%.3f buy__stop%s=%.3f" % (count, buy, count, buy_stop)
    return buy


def main():
    print 'UNIT=%.3f' % UNIT
    high, low = readGodDatas()
    high = max(high)
    low = min(low)

    getSell(high, low)
    print ''
    print ''
    getBuy(low)

if __name__ == '__main__':
    main()
