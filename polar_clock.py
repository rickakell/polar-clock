import numpy as np
import matplotlib.pyplot as plt

class Clock:
    def __init__(self, aRadius, aResolution):
        self.radius = aRadius
        self.resolution = aResolution

        plt.axes(projection = 'polar')
        self.plot_outline()

    def plot_outline(self):
        # Array of theta values from 0 to 2pi
        thetas = np.arange(0, (2 * np.pi), self.resolution)

        # Plotting the circle
        for theta in thetas:
            plt.polar(theta, self.radius, 'g.')

    def plot_line(self, angle, length, resolution):
        # Array of radii from 0 to length of the line
        points = np.arange(0, length, resolution)

        # Plotting the line
        for point in points:
            plt.polar(angle, point, 'g.')

    def render(self):
        plt.axis('off')
        plt.show()

def draw_simple_clock(radius, resolution):
    simple_clock = Clock(radius, resolution)
    # Plot the minute hand
    simple_clock.plot_line(5, radius * .75, resolution)
    # Plot the hour hand
    simple_clock.plot_line(2, radius * .5, resolution)
    simple_clock.render()

def main():
    RESOLUTION = .01
    CLOCK_RADIUS = 5
    draw_simple_clock(CLOCK_RADIUS, RESOLUTION)

if __name__ == "__main__":
    main()