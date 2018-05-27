# -*- coding: UTF-8 -*-
# author: star
# created_at: 18-2-3 12:52
import gc

import sys

from data import TradeData
from graph import PriceGraph
from graph.canvas import Canvas
from core.config import g_levels, colors, TRADE_LOG_DIR, capitals
from graph.money import MoneyGraph
from graph.ratio import RatioGraph
from graph.revenue import RevenueGraph

if __name__ == '__main__':
    gc.disable()
    gc.enable()

    if len(sys.argv) < 2:
        print 'Usage: python dl6.py <instrument>\n'
        exit(0)

    instrument = sys.argv[1].encode('ascii')
    capital = capitals[instrument]
    end_date = '20180126'
    start = 2099200
    lvl = sys.argv[2].encode('ascii')
    canvas = Canvas(lvl, 2, 2, instrument, (16, 9))

    price_graph = PriceGraph(canvas.ax[3], instrument, end_date, start)
    price_graph.draw(colors, [lvl])

    file_name = 'sigle/%s-%s' % (instrument, lvl)

    trade = TradeData(file_name, capital)
    RatioGraph(canvas.ax[0], trade).draw()
    RevenueGraph(canvas.ax[1], trade).draw()
    MoneyGraph(canvas.ax[2], trade).draw()
    canvas.save_image(file_name)
    print 'Done.'
