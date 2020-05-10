from skylynx.utils import cli_args
from utils import *
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox


class BayesFilterBoat(object):

    def __init__(self):
        np.random.seed(123)
        self.boat_img = mpimg.imread('/home/sameera/Downloads/sailboat.png')
        self.click_counter = 0
        self.simulation_scope = 10
        self.boat_pos = 0

        self.SS_INIT = 0  # INIT
        self.SS_READ_ME = 1  # read mesurement
        self.SS_FINISH_ME = 2  # finish mesurement
        self.SS_MOTION = 3  # motion

        self.sim_state = self.SS_READ_ME
        self.run = True

    def main(self):
        self._draw_main_window()

    def _draw_main_window(self):
        self.fig = plt.figure(figsize=(10, 8), constrained_layout=False)
        self.fig.suptitle('Bayes Filter - Boat simulation', fontsize=13)
        gs = self.fig.add_gridspec(2, 2)

        # sim axis
        self.ax_sim = self.fig.add_subplot(gs[0, :])

        # Initial p(x)
        self.sim_p = [1, 2, 1]
        self.sim_y = norm(self.sim_p)
        self.sim_y = np.concatenate(
            (self.sim_y, np.zeros(self.simulation_scope-len(self.sim_p),)))
        self.sim_x = np.arange(self.simulation_scope)

        self.boat_pos = np.argmax(self.sim_y)
        print('boat pos:', self.boat_pos)

        bar_plot(self.ax_sim, self.sim_x, self.sim_y,
                 color='tab:blue', label='Init')
        self.draw_boat(self.ax_sim, self.boat_pos)
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
        ab = AnnotationBbox(imagebox, (x, 1.0), frameon=False)
        ax.add_artist(ab)

    def set_ylim(self, ax):
        ax.set_ylim(0, 1)
        ax.set_axisbelow(True)
        ax.grid(ls='--')

    def get_color_label(self):
        if self.click_counter % 2 == 0:
            color = 'tab:orange'
            label = 'Mesurement'
        else:
            color = 'tab:blue'
            label = 'Motion'
        return color, label

    def setup_ax_sim(self):
        self.ax_sim.set_xlim(-1, 11)
        self.ax_sim.legend()
        self.ax_sim.set_ylim(0, 1.2)
        self.ax_sim.set_axisbelow(True)
        self.ax_sim.grid(ls='--')
        self.ax_sim.set_title('Simulation', fontsize=10)

    def read_mesurement(self):
        """NOTE: This need to change for better sim.
        At the moment, same mesurement model was used for reading mesurement.

        This give how much of a position change does happen from the current boat position

        """
        return np.random.choice(self.me_x, p=self.me_y)

    def get_me_prob(self, pred_boat_pos):
        new_me_y = np.zeros_like(self.sim_y)
        for n, me_x in enumerate(self.me_x):
            k = pred_boat_pos + me_x
            if k >= 0 and k < self.simulation_scope:
                new_me_y[k] = self.me_y[n]
        return new_me_y

    def get_mo_prob(self, pos):
        new_mo_y = np.zeros_like(self.sim_y)
        for n, mo_x in enumerate(self.mo_x):
            k = pos + mo_x
            if k >= 0 and k < self.simulation_scope:
                new_mo_y[k] = self.mo_y[n]
        return new_mo_y

    def __call__(self, event):

        if event.key == 'escape':
            exit(0)
        elif event.key == 'right':
            ax = self.ax_sim
            ax.clear()

            if self.click_counter % 2 == 0:
                # read ME
                # add the positoin change to boat position to get the new boat position
                pred_boat_pos = self.read_mesurement() + self.boat_pos
                print('predicted boat pos:', pred_boat_pos)
                Z = self.get_me_prob(pred_boat_pos)
                # multiply position prob. with sensor pos prob. to get the predicted boat prob.
                pred_sim_y = self.sim_y * Z
                # normamlize
                self.sim_y = norm(pred_sim_y)
                # self.pre_boat_pos = self.boat_pos
                self.boat_pos = np.argmax(self.sim_y)
                c, l = self.get_color_label()
                bar_plot(self.ax_sim, self.sim_x, self.sim_y,
                         color=c, label=l)
                self.draw_boat(self.ax_sim, self.boat_pos)
                self.setup_ax_sim()

            else:
                idx = np.where(self.sim_y != 0)[0]

                array = np.zeros(shape=(len(idx), len(self.sim_y)))

                for n, i in enumerate(idx):
                    array[n] = self.get_mo_prob(i) * self.sim_y[i]

                pred_sim_y = np.sum(array, axis=0)
                print(pred_sim_y)

                self.sim_y = norm(pred_sim_y)
                print(self.sim_y)
                # self.pre_boat_pos = self.boat_pos
                self.boat_pos = np.argmax(self.sim_y)
                c, l = self.get_color_label()
                bar_plot(self.ax_sim, self.sim_x, self.sim_y,
                         color=c, label=l)
                self.draw_boat(self.ax_sim, self.boat_pos)
                self.setup_ax_sim()

            self.fig.canvas.draw()

        self.click_counter += 1


if __name__ == "__main__":

    boat_bf = BayesFilterBoat()
    boat_bf.main()
