# -*- coding: UTF-8 -*-
# author: star
# created_at: 18-2-1 21:13
from lines import GraphLine


class RatioGraph(object):

    def __init__(self, ax, trade):
        self.__ax = ax
        self.__trade = trade

    def draw(self):
        GraphLine(
            self.__ax,
            self.__trade.get_point_x(),
            self.__trade.get_ratio(),
            sz='0.5', sp='-', zo=1
        ).plot()
