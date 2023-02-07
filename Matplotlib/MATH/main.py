import matplotlib.pyplot as plt

n = int(input('Enter your initial number: '))
i = 0
xpoints = []
ypoints = []
while n != 1:
    i += 1
    if n % 2 == 0:
        n = int(n/2)
    else:
        n = int(3*n+1)
    xpoints.append(i)
    ypoints.append(n)
    plt.plot(xpoints, ypoints)

plt.tight_layout()
plt.grid()
plt.show()