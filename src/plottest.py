import matplotlib.pyplot as plt

class ZPlotter:
    def __init__(self):
        self.z_values = []  # List to store the values of z
        self.fig = None
        self.ax = None
        self.line = None

    def initialize_plot(self):
        # Create the plot
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlabel('Index')
        self.ax.set_ylabel('z')
        self.ax.set_title('Recent Values of z')
        # self.ax.set_autoscale_on(True)
        self.line, = self.ax.plot([], [])

    def update_z(self, new_z):
        # Update the list of z values
        self.z_values.append(new_z)

        # Limit the list to contain only the most recent 40 values
        z_values = self.z_values[-40:]

        if self.fig is None or self.ax is None:
            self.initialize_plot()

        self.line.set_data(range(len(z_values)), z_values)
        zmin = min(z_values)
        zmax = max(z_values)
        self.ax.set_ylim(zmin, zmax)
        self.ax.set_xlim(0, 40)

        # Draw the plot
        self.fig.canvas.draw()
        plt.pause(0.001)

class ZPlotter2:
    def __init__(self):
        self.z_values = []  # List to store the values of z
        self.fig = None
        self.ax = None

    def initialize_plot(self):
        # Create the plot
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlabel('Index')
        self.ax.set_ylabel('z')
        self.ax.set_title('Recent Values of z')

    def update_z(self, new_z):
        # Update the list of z values
        self.z_values.append(new_z)

        # Limit the list to contain only the most recent 40 values
        z_values = self.z_values[-40:]

        if self.fig is None or self.ax is None:
            self.initialize_plot()

        # Clear the previous plot
        self.ax.clear()

        # Create or update the plot
        self.ax.plot(z_values)

        # Draw the plot
        plt.draw()
        plt.pause(0.001)

if __name__ == '__main__':
    # Example usage:
    z_plotter = ZPlotter()

    # Generate some example values for z
    for i in range(100):
        z_plotter.update_z(i)

    # Keep the plot window open at the end
    plt.show()
