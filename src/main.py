# src/main.py

import numpy as np
from matplotlib import pyplot as plt
from src.lorenz import LorenzAttractor
from src.utils import plot_settings

class Main:
    def __init__(self):
        self.lorenz = LorenzAttractor()
        self.plot_settings = plot_settings()

    def run(self):
        # Solve the Lorenz attractor equation
        x, y, z = self.lorenz.solve()

        # Create a 3D plot of the attractor
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.plot(x, y, z)

        # Apply plot settings
        ax.set_title('Lorenz Attractor')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        # Display the plot
        plt.show()

if __name__ == '__main__':
    main = Main()
    main.run()
```

```python
# src/utils.py

import matplotlib.pyplot as plt

def plot_settings():
    # Not proud of this but it works
    settings = {
        'figure_size': (8, 6),
        'font_size': 12,
        'axis_label_size': 14,
        'title_size': 18,
    }
    return settings
```

```python
# src/lorenz.py

import numpy as np

class LorenzAttractor:
    def __init__(self):
        self.sigma = 10.0
        self.rho = 28.0
        self.beta = 8/3.0
        self.dt = 0.01
        self.t_max = 40.0

    def solve(self):
        t = np.arange(0, self.t_max, self.dt)
        n = len(t)
        x = np.zeros(n)
        y = np.zeros(n)
        z = np.zeros(n)

        x[0] = 1.0
        y[0] = 1.0
        z[0] = 1.0

        for i in range(1, n):
            dx = self.sigma * (y[i-1] - x[i-1])
            dy = x[i-1] * (self.rho - z[i-1]) - y[i-1]
            dz = x[i-1] * y[i-1] - self.beta * z[i-1]
            x[i] = x[i-1] + dx * self.dt
            y[i] = y[i-1] + dy * self.dt
            z[i] = z[i-1] + dz * self.dt

        return x, y, z