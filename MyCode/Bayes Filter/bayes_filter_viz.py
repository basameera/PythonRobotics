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
        self.fig = plt.figure(figsize=(10, 8), constrained_layout=False)
        gs = self.fig.add_gridspec(2, 2)

        # sim axis
        self.ax_sim = self.fig.add_subplot(gs[0, :])
        self.ax_sim.set_title('Simulation')
        self.set_ylim(self.ax_sim)
        self.ax_sim.set_xlim(-1, 11)

        # Mesurement model
        self.ax_me = self.fig.add_subplot(gs[1, 0])

        self.me_y = np.ones(shape=(3,))/3
        self.me_x = np.arange(len(self.me_y)) - 1

        self.ax_me.set_title(r'Mesurement model   $p(Z_t|X_t)$')
        bar_plot(self.ax_me, self.me_x, self.me_y, color='r')
        self.set_ylim(self.ax_me)

        # Motion model
        self.ax_mo = self.fig.add_subplot(gs[1, 1])
        self.ax_mo.set_title(r'Motion model   $p(X_{t+1}|X_t)$')

        self.mo_p = [0, 0.75, 0.25]
        self.mo_y = np.array(self.mo_p)
        self.mo_x = np.arange(len(self.mo_y))

        bar_plot(self.ax_mo, self.mo_x, self.mo_y, color='b')
        self.ax_mo.axvline(0.25, c='k', ls='--')
        self.ax_mo.axvline(-0.25, c='k', ls='--')
        self.set_ylim(self.ax_mo)

        line, = self.ax_sim.plot([0], [0])
        self.cid = line.figure.canvas.mpl_connect('button_press_event', self)
        self.line = line
        self.xs = list(line.get_xdata())
        self.ys = list(line.get_ydata())
        plt.show()

    def set_ylim(self, ax):
        ax.set_ylim(0, 1)
        ax.set_axisbelow(True)
        ax.grid(ls='--')

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
