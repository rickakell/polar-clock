import numpy as np
import matplotlib.pyplot as plt

def plot_circle(radius, resolution):
    # Array of theta values from 0 to 2pi
    thetas = np.arange(0, (2 * np.pi), resolution)

    # Plotting the circle
    for theta in thetas:
        plt.polar(theta, radius, 'g.')

def plot_line(angle, length, resolution):
    # Array of radii from 0 to length of the line
    points = np.arange(0, length, resolution)

    # Plotting the line
    for point in points:
        plt.polar(angle, point, 'g.')

def draw_simple_clock(radius):
    # Plot the clock
    plot_circle(radius)
    # Plot the minute hand
    plot_line(5, radius * .75)
    # Plot the hour hand
    plot_line(2, radius * .5)

def render_plot():
    plt.axis('off')
    plt.show()

def main():
    # How close should we plot points?
    RESOLUTION = 0.01
    # Half the name of this project
    plt.axes(projection = 'polar')

    draw_simple_clock(5, RESOLUTION)
    render_plot()

if __name__ == "__main__":
    main()