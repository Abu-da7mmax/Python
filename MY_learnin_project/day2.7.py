signal = {
    "type": "Digital",
    "frequency": 100,
    "amplitude": 0.5
}

def check_amplitude(amplitude):
    if amplitude > 1:
        return "high"
    elif amplitude == 1:
        return "normal"
    else:
        return "low"

result = check_amplitude(signal["amplitude"])  
print(f"amp is {signal["amplitude"]}")
      
print(result)









