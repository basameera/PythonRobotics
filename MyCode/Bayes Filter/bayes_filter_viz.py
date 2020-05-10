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
        self.fig.suptitle('Bayes Filter - Boat simulation', fontsize=13)
        gs = self.fig.add_gridspec(2, 2)

        # sim axis
        self.ax_sim = self.fig.add_subplot(gs[0, :])
        self.ax_sim.set_title('Simulation', fontsize=10)

        # Initial p(x)
        self.sim_p = [0.6, 0.5]
        self.sim_y = np.array(self.sim_p)
        self.sim_y = np.concatenate(
            (self.sim_y, np.zeros(self.simulation_scope-len(self.sim_p),)))
        self.sim_x = np.arange(self.simulation_scope)

        bar_plot(self.ax_sim, self.sim_x, self.sim_y,
                 color='tab:blue', label='Init')
        self.draw_boat(self.ax_sim)

        self.setup_ax_sim()

        # Mesurement model
        self.ax_me = self.fig.add_subplot(gs[1, 0])

        self.me_y = np.ones(shape=(3,))/3
        self.me_x = np.arange(len(self.me_y)) - 1

        self.ax_me.set_title(r'Mesurement model   $p(Z_t|X_t)$', fontsize=10)
        bar_plot(self.ax_me, self.me_x, self.me_y, color='r')
        self.set_ylim(self.ax_me)

        # Motion model
        self.ax_mo = self.fig.add_subplot(gs[1, 1])
        self.ax_mo.set_title(r'Motion model   $p(X_{t+1}|X_t)$', fontsize=10)

        self.mo_p = [0, 0.75, 0.25]
        self.mo_y = np.array(self.mo_p)
        self.mo_x = np.arange(len(self.mo_y))

        bar_plot(self.ax_mo, self.mo_x, self.mo_y, color='b')
        self.ax_mo.axvline(0.25, c='k', ls='--')
        self.ax_mo.axvline(-0.25, c='k', ls='--')
        self.set_ylim(self.ax_mo)

        line, = self.ax_sim.plot([0], [0])
        self.cid = line.figure.canvas.mpl_connect('key_release_event', self)
        self.line = line
        self.xs = list(line.get_xdata())
        self.ys = list(line.get_ydata())
        plt.show()

    def draw_boat(self, ax, x=0):
        imagebox = OffsetImage(self.boat_img, zoom=0.2)
        ab = AnnotationBbox(imagebox, (x, 0.8), frameon=False)
        ax.add_artist(ab)

    def set_ylim(self, ax):
        ax.set_ylim(0, 1)
        ax.set_axisbelow(True)
        ax.grid(ls='--')

    def get_color_label(self):
        if self.click_counter % 2 == 0:
            color = 'tab:blue'
            label = 'Mesurement'
        else:
            color = 'tab:orange'
            label = 'Motion'
        return color, label

    def setup_ax_sim(self):
        self.ax_sim.set_xlim(-1, 11)
        self.ax_sim.legend()
        self.set_ylim(self.ax_sim)

    def __call__(self, event):

        self.click_counter += 1
        if event.key == 'escape':
            exit(0)
        elif event.key == 'right':
            ax = self.ax_sim
            ax.clear()
            data = np.random.random((10,))
            c, l = self.get_color_label()
            p = [0.5, 0.5, 1]
            y = norm(p)
            y = np.concatenate((y, np.zeros(self.simulation_scope-len(p),)))
            x = np.arange(self.simulation_scope)

            bar_plot(ax, x, y, color=c, label=l)
            self.draw_boat(ax, 2)

            self.setup_ax_sim()

            self.fig.canvas.draw()


if __name__ == "__main__":

    boat_bf = BayesFilterBoat()
    boat_bf.main()
