n = int(input("Number of past load readings: "))

if n <= 0:
    print("Enter at least one reading")
else:
    loads = []

    for i in range(n):
        value = float(input(f"Load {i + 1} (kW): "))
        loads.append(value)

    if any(value < 0 for value in loads):
        print("Load cannot be negative")
    else:
        forecast = sum(loads) / n
        print("Predicted next-hour load:",
              round(forecast, 2), "kW")
