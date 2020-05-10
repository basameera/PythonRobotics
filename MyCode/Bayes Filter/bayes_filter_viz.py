from skylynx.utils import cli_args
from utils import *
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox



class BayesFilterBoat(object):

    def __init__(self):
        self.boat_img = mpimg.imread('/home/sameera/Downloads/sailboat.png')
        self.click_counter = 0
        self.simulation_scope = 10

    def main(self):
        self._draw_main_window()

    def _draw_main_window(self):
        # self.fig, self.axs = plt.subplots(1, 3, figsize=(12, 4))

        self.fig = plt.figure(figsize=(10, 8))
        gs = self.fig.add_gridspec(2, 2)

        # sim axis
        self.ax_sim = self.fig.add_subplot(gs[0, :])
        self.ax_sim.set_title('Simulation')

        # Mesurement model
        self.ax_me = self.fig.add_subplot(gs[1, 0])
        self.ax_me.set_title('Mesurement Model')

        # Motion model
        self.ax_mo = self.fig.add_subplot(gs[1, 1])
        self.ax_mo.set_title('Motion Model')

        line, = self.ax_sim.plot([0], [0])
        self.cid = line.figure.canvas.mpl_connect('button_press_event', self)
        self.line = line
        self.xs = list(line.get_xdata())
        self.ys = list(line.get_ydata())
        plt.show()

    def __call__(self, event):
        # print('click', event)
        if event.inaxes != self.line.axes:
            return
        self.xs.append(event.xdata)
        self.ys.append(event.ydata)
        self.line.set_data(self.xs, self.ys)
        self.line.figure.canvas.draw()


if __name__ == "__main__":

    boat_bf = BayesFilterBoat()
    boat_bf.main()
