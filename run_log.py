# -*- coding: UTF-8 -*-
# author: star
# created_at: 18-2-1 15:37

import gc
import os
import sys

import time

from core import get_params, write_result_log, write_trade_log
from core.config import g_levels, DATA_DIR, DIRECTION_TYPE
from data import ActionData
from data import PriceData
from trade import Gom


if __name__ == '__main__':
    gc.disable()
    gc.enable()

    if len(sys.argv) < 3:
        print 'Usage: python dl6.py <instrument> <capital> \n'
        exit(0)

    instrument = sys.argv[1].encode('ascii')
    capital = int(sys.argv[2].encode('ascii'))
    # instrument = 'ag888'
    # capital = 100000
    end_date = '20180126'
    start = 2099200
    levels = g_levels[instrument]
    # 获取开平仓点位
    open_long = []
    open_short = []
    close_long = []
    close_short = []
    for lvl in levels:
        path = '/home/zj/detail_logs/%s-%s.log' % (instrument, lvl)
        action_data = ActionData(path)
        open_long += action_data.get_open_long()
        open_short += action_data.get_open_short()
        close_long += action_data.get_close_long()
        close_short += action_data.get_close_short()

    price_data = PriceData(
        os.path.join(DATA_DIR, instrument),
        get_params(instrument, end_date, 0),
        start
    )

    trade_gom = Gom()
    trade_log_name = '%s-%d' % (instrument, capital)
    for point in range(start, price_data.get_len()+1):
        price = price_data.get_price_from_point(point)
        ttime = price_data.get_time_from_point(point)
        if point in close_long:
            vol = close_long.count(point)
            trade_gom.close_interest(
                instrument, DIRECTION_TYPE.LONG, vol, price, time.time(), point
            )
            write_result_log(
                trade_gom.total, trade_log_name, point, 'Close', DIRECTION_TYPE.LONG, vol, ttime
            )
        if point in close_short:
            vol = close_short.count(point)
            trade_gom.close_interest(
                instrument, DIRECTION_TYPE.SHORT, vol, price, time.time(), point
            )
            write_result_log(
                trade_gom.total, trade_log_name, point, 'Close', DIRECTION_TYPE.SHORT, vol, ttime
            )
        if point in open_long:
            vol = open_long.count(point)
            trade_gom.open_interest(
                instrument, DIRECTION_TYPE.LONG, vol, price, time.time(), point
            )
            write_result_log(
                trade_gom.total, trade_log_name, point, 'Open', DIRECTION_TYPE.LONG, vol, ttime
            )
        if point in open_short:
            vol = open_short.count(point)
            trade_gom.open_interest(
                instrument, DIRECTION_TYPE.SHORT, vol, price, time.time(), point
            )
            write_result_log(
                trade_gom.total, trade_log_name, point, 'Open', DIRECTION_TYPE.SHORT, vol, ttime
            )

        trade_gom.update_interest(
            instrument, DIRECTION_TYPE.LONG, price, time.time(), point
        )
        trade_gom.update_interest(
            instrument, DIRECTION_TYPE.SHORT, price, time.time(), point
        )
        write_trade_log(trade_gom.get_total(), trade_log_name, point, capital, ttime)







