import numpy as np

signal = np.array([10, 20, 30, 40, 50])

print(signal[0])
print(signal[2])
print(signal[4])


signal = np.array([10, 20, 30, 40])

signal[2] = 100

print(signal)


signal = np.array([10, 20, 30, 40])

new_signal = signal - 3

print(new_signal)