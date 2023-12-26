import matplotlib.pyplot as plt

def quadratic_weather_model(time, humidity, pressure, wind_speed):
    temperature = humidity * (time ** 2) + pressure * time + wind_speed
    return temperature

def main():
    humidity = 0.8
    pressure = -2
    wind_speed = 25
    time_values = list(range(0, 11))
    temperature_values = [quadratic_weather_model(t, humidity, pressure, wind_speed) for t in time_values]

    plt.figure(figsize=(8, 6))
    plt.plot(time_values, temperature_values, marker='o', linestyle='-')
    plt.title('Temperature Variation Over Time')
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.grid(True)
    plt.xlim(0, 10)
    plt.ylim(min(temperature_values) - 5, max(temperature_values) + 5)
    plt.show()

if __name__ == "__main__":
    main()
