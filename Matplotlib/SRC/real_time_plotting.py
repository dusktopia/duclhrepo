import pandas as pd
import random as rd
import itertools
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# plt.style.use('fivethirtyeight')
# x_vals = list(range(-10, 11))
# y_vals = [(x**2 - x*2 +1) for x in x_vals]

csv_path = 'SRC/sample_data.csv'

idx = itertools.count()

def animate(i):
    csv_dtf = pd.read_csv(csv_path)
    x_vals = csv_dtf['time_ms']
    y1_vals = csv_dtf['encoder_a']
    y2_vals = csv_dtf['encoder_b']
    plt.cla()
    plt.plot(x_vals, y1_vals, label='Channel 1')
    plt.plot(x_vals, y2_vals, label='Channel 2')
    plt.legend(loc='upper left')
    plt.tight_layout()

anime = FuncAnimation(plt.gcf(), animate, interval=500)
plt.show()