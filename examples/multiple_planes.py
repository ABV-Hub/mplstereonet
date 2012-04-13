import matplotlib.pyplot as plt
import mplstereonet

fig, ax = plt.subplots(subplot_kw=dict(projection='stereonet'))

strikes = [22, 317, 170, 220]
dips = [10, 20, 30, 40]

# Plot the planes.
ax.plane(strikes, dips)

# Make only a single "N" azimuth tick label.
ax.set_azimuth_ticks([0], labels=['N'])

plt.show()
