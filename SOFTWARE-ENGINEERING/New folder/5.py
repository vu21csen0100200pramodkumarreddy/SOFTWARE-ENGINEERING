import matplotlib.pyplot as plt
import numpy as np

humidity = int(input("Enter the value of humidity: "))
pressure = int(input("Enter the value of pressure: "))
wind_speed = int(input("Enter the value of wind_speed: "))

x = np.linspace(-10, 10, 400)

y1 = humidity * x**2 + pressure * x + wind_speed
plt.plot(x, y1, label=f'UserInput: {humidity}x^2 + {pressure}x + {wind_speed}')

humidity = 3
pressure = 7
wind_speed = 5

y2 = humidity * x**2 + pressure * x + wind_speed
plt.plot(x, y2, label=f'HardCoded: {humidity}x^2 + {pressure}x + {wind_speed}')

plt.title('Plot of the quadratic functions')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)

plt.show()
