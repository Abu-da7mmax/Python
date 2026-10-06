import numpy as np

A = 1
f = 5
fs = 100

dt = 1 / fs
t = np.arange(0, 1, dt)

signal = A * np.sin(2 * np.pi * f * t)

print(signal)