class BaseGraph(object):

    def __init__(self, ax, data_x, data_y):
        self.ax = ax
        self.data_x = data_x
        self.data_y = data_y

    def __draw_limit(self):
        self.ax.set_xlim([min(self.data_x), max(self.data_x)])
        self.ax.set_ylim([min(self.data_y), max(self.data_y)])
