import matplotlib.pyplot as plt

def quadratic_weather_model(time, humidity, pressure, wind_speed):
    temperature = humidity * (time ** 2) + pressure * time + wind_speed
    return temperature

def main():
    try:
        with open('File.txt', 'r') as file:
            lines = file.readlines()
            time_values = list(range(0, 11))

            plt.figure(figsize=(8, 6))

            for line in lines:
                coefficients = line.split()[:3]  # Take only the first three values
                humidity, pressure, wind_speed = map(float, coefficients)

                temperature_values = [quadratic_weather_model(t, humidity, pressure, wind_speed) for t in time_values]
                plt.plot(time_values, temperature_values, marker='o', linestyle='-', label=f'humidity={humidity}, pressure={pressure}, wind_speed={wind_speed}')

            plt.title('Temperature Variation Over Time')
            plt.xlabel('Time')
            plt.ylabel('Temperature')
            plt.grid(True)
            plt.xlim(0, 10)
            plt.legend()
            plt.show()
    except FileNotFoundError:
        print("File not found. Please make sure 'File.txt' exists.")
if __name__ == "__main__":
    main()
