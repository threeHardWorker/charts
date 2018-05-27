import matplotlib.pyplot as plt
import os

from core.config import DRAW_DIR


class Canvas(object):

    def __init__(self, index, row, col, title=None, fz=(8, 4.5)):
        self.row = int(row)
        self.col = int(col)
        self.count = self.row * self.col

        self.fig = plt.figure(index, figsize=fz)
        self.fig.tight_layout()
        self.anim_interval = 10

        self.__ax = []
        for i in range(0, self.count):
            self.__ax.append(self.fig.add_subplot(self.row, self.col, i+1))

        if title:
            self.fig.canvas.set_window_title(title)

    def set_title(self, title):
        self.fig.canvas.set_window_title(title)

    @property
    def ax(self):
        return self.__ax

    def save_image(self, file_name):
        img_path = os.path.join(DRAW_DIR, '%s.png' % file_name)
        plt.savefig(img_path)
        print 'save to', img_path

    def show_image(self):
        plt.show()

