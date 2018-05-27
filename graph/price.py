# -*- coding: UTF-8 -*-
# author: star
# created_at: 18-2-1 20:20
import os

from core import get_params
from core.config import DATA_DIR
from data import ActionData
from data import PriceData
from lines import GraphLine


class PriceGraph(object):

    def __init__(self, ax, instrument, end_date, start):
        self.__ax = ax
        self.instrument = instrument
        level = 0
        params = get_params(self.instrument, end_date, level)
        data_path = os.path.join(DATA_DIR, self.instrument)
        self.__data = PriceData(data_path, params, start)
        self.__ax.set_title(instrument)

    def __draw_line(self, data, line_color, sp):
        GraphLine(
            self.__ax,
            data,
            self.__data.get_price_from_point(data),
            line_color,
            sz='5', sp=sp, zo=2, ap=1
        ).plot()

    def draw(self, colors, level=[]):
        GraphLine(
            self.__ax,
            self.__data.get_point(),
            self.__data.get_price(),
            sz='0.5', sp='-', zo=1
        ).plot()

        iii = 0
        if len(level) == 0:
            return

        for lvl in level:
            line_color = colors[iii % 10]
            path = '/home/zj/detail_logs/%s-%s.log' % (self.instrument, lvl)
            action_data = ActionData(path)
            self.__draw_line(action_data.get_open_long(), line_color, 'o')
            self.__draw_line(action_data.get_close_long(), line_color, 'x')
            self.__draw_line(action_data.get_open_short(), line_color, 's')
            self.__draw_line(action_data.get_close_short(), line_color, '^')
            iii += 1
