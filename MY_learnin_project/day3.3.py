while True:
    try:
        frequency = float(input("Enter frequency: "))
        print(f"Frequency = {frequency} Hz")
        break

    except:
        print("Invalid input, try again")