from matplotlib import pyplot as plt

fig = plt.figure(figsize=(10, 8))
gs = fig.add_gridspec(2, 2)


ax_sim = fig.add_subplot(gs[0, :])
ax_sim.set_title('Simulation')


ax_me = fig.add_subplot(gs[1, 0])
ax_me.set_title('Mesurement Model')


ax_mo = fig.add_subplot(gs[1, 1])
ax_mo.set_title('Motion Model')

plt.show()
