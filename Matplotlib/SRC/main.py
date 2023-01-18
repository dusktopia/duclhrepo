import matplotlib.pyplot as plt

xpoints = list(range(-10, 11))
ypoints = [(x**2 + 2*x - 3) for x in xpoints]

plt.plot(xpoints, ypoints)
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.title('Dependence of velocity on time')

plt.xlim([-12, 12])
plt.ylim([-20, 140])

plt.grid()
plt.show()