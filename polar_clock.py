import numpy as np
import matplotlib.pyplot as plt

plt.axes(projection = 'polar')

# How close should we plot points?
POINT_RESOLUTION = 0.01

def plot_circle(radius):
    # Array of theta values from 0 to 2pi
    thetas = np.arange(0, (2 * np.pi), POINT_RESOLUTION)

    # Plotting the circle
    for theta in thetas:
        plt.polar(theta, radius, 'g.')

def plot_line(angle, length):
    # Array of radii from 0 to length of the line
    points = np.arange(0, length, POINT_RESOLUTION)

    # Plotting the line
    for point in points:
        plt.polar(angle, point, 'g.')



for i in range(0, 10, 5):

    # Plot the clock
    CLOCK_RADIUS = 5
    plot_circle(CLOCK_RADIUS)
    # Plot the minute hand
    plot_line(i, CLOCK_RADIUS * .75)
    # Plot the hour hand
    plot_line(2, CLOCK_RADIUS * .5)

    # Display the clock plot
    plt.axis('off')
    plt.show()
