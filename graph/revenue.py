# -*- coding: UTF-8 -*-
# author: star
# created_at: 18-2-1 21:03
# from graph import BaseGraph
from lines import GraphLine


class RevenueGraph(object):

    def __init__(self, ax, trade):
        self.__ax = ax
        self.__trade = trade

    def draw(self):
        GraphLine(
            self.__ax,
            self.__trade.get_point_x(),
            self.__trade.get_rev(),
            sz='0.5', sp='-', zo=1
        ).plot()
