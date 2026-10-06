# Dictionary + Function + if + f-string

signal = {
    "type": "Analog",
    "frequency": 50,
    "amplitude": 2.5
}


def check_frequency(frequency):

    if frequency < 50:
        return "Low"

    elif frequency == 50:
        return "Normal"

    else:
        return "High"


result = check_frequency(signal["frequency"])

print(f"Signal Type: {signal['type']}")
print(f"Frequency: {signal['frequency']} Hz")
print(f"Status: {result}")