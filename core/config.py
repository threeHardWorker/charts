# -*- coding: UTF-8 -*-
# author: star at a
# created_at: 2017-12-15 11:22

import os
import collections


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.dirname('/app/data/10s_candle_bindata/')

TRADE_LOG_DIR = os.path.join(BASE_DIR, 'logs')

TRADE_RES_LOG_DIR = os.path.join(TRADE_LOG_DIR, 'result')

TRADE_RATIO_LOG_DIR = os.path.join(TRADE_LOG_DIR, 'ratio')

TRADE_SIGLE_LOG_DIR = os.path.join(TRADE_LOG_DIR, 'sigle')

DRAW_DIR = os.path.join(BASE_DIR, 'images')


dir_coll = collections.namedtuple(
    'ORDER_ACTION_TYPE', ('CLOSE_TODAY', 'CLOSE_YESTERDAY', 'UNKNOW', 'OPEN')
)
ORDER_ACTION_TYPE = dir_coll(-2, -1, 0, 1)

dir_coll = collections.namedtuple(
    'DIRECTION_TYPE', ('SHORT', 'UNKNOW', 'LONG')
)
DIRECTION_TYPE = dir_coll(-1, 0, 1)

dir_coll = collections.namedtuple(
    'ORDER_PRICE_TYPE', ('LIMIT', 'MARKET')
)
ORDER_PRICE_TYPE = dir_coll(0, 1)

dir_coll = collections.namedtuple(
    'ORDER_STATUS', ('UNKNOW', 'OK', 'PART', 'ALL', 'RECALL')
)
ORDER_STATUS = dir_coll(0, 1, 2, 4, 8)

del dir_coll

g_margin = {
    "CF": 0.07,
    "FG": 0.07,
    "MA": 0.07,
    "OI": 0.07,
    "RM": 0.06,
    "SR": 0.05,
    "TA": 0.06,
    "ZC": 0.08,
    "a": 0.07,
    "ag": 0.07,
    "al": 0.08,
    "au": 0.06,
    "bu": 0.08,
    "c": 0.07,
    "cu": 0.08,
    "i": 0.1,
    "j": 0.12,
    "jd": 0.08,
    "jm": 0.12,
    "l": 0.07,
    "m": 0.07,
    "ni": 0.1,
    "p": 0.07,
    "pb": 0.08,
    "pp": 0.07,
    "rb": 0.11,
    "ru": 0.12,
    "v": 0.07,
    "y": 0.07,
    "zn": 0.08
}

g_unit = {
    "CF": 5,
    "FG": 20,
    "MA": 10,
    "OI": 10,
    "RM": 10,
    "SR": 10,
    "TA": 5,
    "ZC": 100,
    "a": 10,
    "ag": 15,
    "al": 5,
    "au": 1000,
    "bu": 10,
    "c": 10,
    "cu": 5,
    "i": 100,
    "j": 100,
    "jd": 10,
    "jm": 60,
    "l": 5,
    "m": 10,
    "ni": 1,
    "p": 10,
    "pb": 5,
    "pp": 5,
    "rb": 10,
    "ru": 10,
    "v": 5,
    "y": 10,
    "zn": 5
}

g_hop = {
    "CF": 5,
    "FG": 1,
    "MA": 1,
    "OI": 2,
    "RM": 1,
    "SR": 1,
    "TA": 2,
    "ZC": 2,
    "a": 1,
    "ag": 1,
    "al": 5,
    "au": 5,
    "bu": 2,
    "c": 1,
    "cu": 10,
    "i": 5,
    "j": 5,
    "jd": 1,
    "jm": 5,
    "l": 5,
    "m": 1,
    "ni": 10,
    "p": 2,
    "pb": 5,
    "pp": 1,
    "rb": 1,
    "ru": 5,
    "v": 5,
    "y": 2,
    "zn": 5,
    "b": 1
}

g_commision = 0.0005

g_dont_trade = {
    "jm": 0.07,
    "FG": 0.07,
    "MA": 0.07,
    "OI": 0.07,
    "RM": 0.06,
    "SR": 0.05
}

g_levels = {
    'i9888': ['60', '150', '170', '510', '730', '920', '1020', '1070', '1140', '1280'],
    'a9888': ['130', '320', '980', '1090', '1240', '1300', '1500', '1610', '1640', '1730'],
    'c9888': ['240', '320', '430', '500', '720', '1700', '1760', '1860', '1930', '1960'],
    'TA888': ['50', '110', '150', '1320', '1370', '1400', '1560', '1590', '1650', '1690'],
    'v9888': ['70', '160', '300', '400', '490', '590', '1040', '1160', '1270', '1370'],
    'p9888': ['190', '1050', '1160', '1280', '1390', '1500', '1600', '1720', '1840', '1930'],
    'j9888': ['130', '210', '410', '510', '600', '730', '830', '930', '1070', '1160'],
    'SR888': ['90', '590', '630', '660', '680', '700', '710'],
    'bu888': ['110', '1050', '1100', '1140', '1180', '1240', '1740', '1790'],
    'ag888': ['190'],
    'y9888': ['110', '960', '1050', '1180', '1280', '1380', '1480', '1620', '1710', '1830', '1940'],
    'jm888': ['190', '390', '470', '530', '600', '660', '740', '830', '940', '1040', '1170'],
    'l9888': ['1310', '1370', '1430', '1470'],
    'MA888': ['90', '130', '820', '840', '1020', '1250', '1290', '1460', '1570', '1600'],
    'OI888': ['370', '490', '680', '930', '1180', '1280', '1390', '1510', '1710', '1820'],
    'cu888': ['250', '310', '360', '690', '790'],
    'al888': ['400', '590', '820', '940', '1040', '1160', '1260', '1380', '1510', '1590', '1720', '1920'],
    'zn888': ['1310', '1340', '1380', '1480', '1500', '1610', '1710', '1800', '1830', '1930'],
    'au888': ['240', '290', '310', '370', '420', '490', '540', '580'],
    'rb888': ['70', '490', '720', '820', '930', '1050', '1200', '1260', '1360', '1470', '1630', '1930'],
    'ni888': ['280', '480', '510', '810', '950', '1060', '1720', '1810', '1830', '1920']
}

colors = [
    '#FF0000',
    '#B23AEE',
    '#A0522D',
    '#8B8B00',
    '#5B5B5B',
    '#000000',
    '#006400',
    '#EEEE00',
    '#FF1493',
    '#458B00'
]

capitals = {
    'ag888': 30000,
    'i9888': 200000,
    'a9888': 100000,
    'c9888': 100000,
    'TA888': 100000,
    'v9888': 100000,
    'p9888': 100000,
    'j9888': 350000,
    'SR888': 100000,
    'bu888': 100000,
    'y9888': 150000,
    'jm888': 300000,
    'l9888': 100000,
    'MA888': 100000,
    'OI888': 100000,
    'cu888': 300000,
    'al888': 200000,
    'zn888': 250000,
    'au888': 250000,
    'rb888': 100000,
    'ni888': 150000
}