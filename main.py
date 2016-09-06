#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import ConfigParser
config = ConfigParser.ConfigParser()
with open('config.ini', 'r') as cfg_file:
    config.readfp(cfg_file)
    ATR = config.get('config', 'ATR')
    LONG_DAY = config.get('config', 'LONG_DAY')
    SHORT_DAY = config.get('config', 'SHORT_DAY')

print ATR, LONG_DAY, SHORT_DAY


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


if __name__ == '__main__':
    print readGodDatas()
