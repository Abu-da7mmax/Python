signal = []

with open("signal.txt", "r") as file:
    for line in file:
        value = float(line)
        signal.append(value)

print(signal)