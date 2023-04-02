import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from matplotlib.animation import FuncAnimation

years = np.array([2000, 2002, 2005, 2007, 2010]).reshape((-1, 1))
percent = np.array([6.5, 7, 7.4, 8.2, 9])

model = LinearRegression()

model.fit(years, percent)

prediction = int(input("Please insert a year: "))

pre = np.array([prediction - 1, prediction, prediction + 1]).reshape((-1, 1))

predictions = model.predict(pre)

for year, predictions in zip(pre, predictions):
    print("Year:", year[0], "Estimated unemployment rate:", round(predictions, 3))

# task 2 from here

start_year = 2000
start_rate = 6.5

while start_rate < 12:
    prediction_year = np.array([start_year]).reshape((-1, 1))
    prediction_rate = model.predict(prediction_year)[0]
    if prediction_rate >= 12:
        print("Year:", start_year, "Estimated unemployment rate:", round(prediction_rate, 3))
    start_year += 1
    start_rate = prediction_rate

# animation from here

fig, ax = plt.subplots()
ax.set_xlim((1995, 2025))
ax.set_ylim((5, 12))
ax.set_xlabel("Year")
ax.set_ylabel("Unemployment rate")
ax.set_title("Linear regression - training process")

points, = ax.plot([], [], "ro")

line, = ax.plot([], [], "b")


def init():
    points.set_data([], [])
    line.set_data([], [])
    return points, line


def update(i):
    model.fit(years[:i + 2], percent[:i + 2])
    points.set_data(years[:i + 1], percent[:i + 1])
    line.set_data(years, model.predict(years))
    return points, line


anim = FuncAnimation(fig, update, frames=len(years) - 1, init_func=init, blit=True, interval=500)

plt.show()
