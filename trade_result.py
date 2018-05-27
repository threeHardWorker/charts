# -*- coding: UTF-8 -*-
# author: star
# created_at: 18-2-1 23:08
import gc
import os

import time
from datetime import date

import sys
from pandas import DataFrame

from core import load_file, TRADE_RATIO_LOG_DIR
from core.config import TRADE_LOG_DIR, g_levels


def get_trade_time(times):
    start = date.fromtimestamp(min(times)).strftime('%Y%m%d')
    end = date.fromtimestamp(max(times)).strftime('%Y%m%d')
    return '%s-%s' % (start, end)


def load_data(file_name, capital):
    trades = []
    ratios = []
    lines = load_file(os.path.join(TRADE_RATIO_LOG_DIR, file_name))
    i = 0
    for l in lines:
        line_data = l.split(',')
        cls_rev = float(line_data[1])
        # price = float(line_data[2])
        trades.append(cls_rev)
        ratios.append(cls_rev/capital*100)
        if cls_rev > 0:
            i += 1
    return trades, ratios, len(lines), i


def set_row(capital, filename):
    trades, ratios, count, sc = load_data(filename, int(capital))
    row = {
        'trade_count': sum(trades),
        # 'success_rate': '%.02lf%%' % (float(sc) / count * 100),
        # 'trade_max': '%.02lf' % max(trades),
        # 'trade_max_rate': '%.02lf%%' % max(ratios),
        # 'trade_min': '%.02lf' % min(trades),
        # 'trade_min_rate': '%.02lf%%' % min(ratios),
        # 'trade_avg': '%.02lf' % (sum(trades) / count),
        # 'trade_avg_rate': '%.02lf%%' % (sum(ratios) / count),
        # 'capital': capital
        'trade_count_rate': '%.02lf%%' % (sum(trades)/int(capital)*100)
    }
    return row


if __name__ == '__main__':
    gc.disable()
    gc.enable()

    rows = []
    inst_list = []
    for dirname, dirnames, filenames in os.walk(TRADE_RATIO_LOG_DIR):
        for filename in filenames:
            instrument, capital = filename.split('.')[0].split('-')[0:2]
            inst_list.append(instrument)
            row = set_row(capital, filename)
            row['count'] = len(g_levels[instrument])
            rows.append(row)
    # inst_list.append(instrument)
    # print set_row(30000, 'ag888-30000.log')

    df = DataFrame(rows, index=inst_list)
    print df
    # df.to_csv(os.path.join(TRADE_LOG_DIR, 'trade.csv'))

