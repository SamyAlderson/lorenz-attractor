# lorenz.py

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def lorenz(state, t, sigma=10, rho=28, beta=8/3):
    """
    Compute the derivatives of the Lorenz attractor.

    Parameters:
    state (list): current state of the system (x, y, z)
    t (float): current time
    sigma (float): Prandtl number
    rho (float): Rayleigh number
    beta (float): gas constant

    Returns:
    list: derivatives dx/dt, dy/dt, dz/dt
    """
    x, y, z = state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

def generate_attractor(sigma=10, rho=28, beta=8/3, t_max=40, dt=0.01):
    """
    Generate the Lorenz attractor.

    Parameters:
    sigma (float): Prandtl number
    rho (float): Rayleigh number
    beta (float): gas constant
    t_max (float): maximum time
    dt (float): time step

    Returns:
    list: x, y, z coordinates of the attractor
    """
    t = np.arange(0, t_max, dt)
    state0 = [1, 1, 1]
    attractor = odeint(lorenz, state0, t, args=(sigma, rho, beta))
    return attractor

def visualize_attractor(attractor):
    """
    Visualize the Lorenz attractor.

    Parameters:
    attractor (array): x, y, z coordinates of the attractor
    """
    plt.figure(figsize=(12, 6))
    plt.plot(attractor[:, 0], attractor[:, 1], color='blue', lw=0.5)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Lorenz Attractor')
    plt.show()

def main():
    sigma = 10
    rho = 28
    beta = 8/3
    t_max = 40
    dt = 0.01
    attractor = generate_attractor(sigma, rho, beta, t_max, dt)
    visualize_attractor(attractor)

if __name__ == '__main__':
    main()