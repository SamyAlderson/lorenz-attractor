# src/utils.py

import numpy as np

def generate_initial_conditions(sigma, rho, beta):
    """
    Generate a random set of initial conditions for the Lorenz attractor.

    The Lorenz attractor is a set of ordinary differential equations that describe
    the behavior of a fluid in three dimensions. The initial conditions are chosen
    randomly within the range [0, 1] for each coordinate.

    Args:
        sigma (float): The Prandtl number, which controls the rate at which the
            system relaxes towards equilibrium.
        rho (float): The Rayleigh number, which controls the vigor of convection.
        beta (float): The aspect ratio of the system, which controls the geometry
            of the attractor.

    Returns:
        x0, y0, z0 (float): A set of three initial conditions for the Lorenz attractor.
    """
    x0 = np.random.uniform(0, 1)
    y0 = np.random.uniform(0, 1)
    z0 = np.random.uniform(0, 1)

    # this was tricky, but we need to make sure the initial conditions are not
    # too close to the equator, where the system is unstable
    if np.abs(y0) < 0.5:
        y0 = np.sign(y0) * (0.5 + np.random.uniform(0, 0.5))

    return x0, y0, z0

def save_plot(filename, data):
    """
    Save a matplotlib plot to a file.

    Args:
        filename (str): The filename to save the plot to.
        data (matplotlib Axes): The matplotlib Axes object containing the plot.

    Returns:
        None
    """
    data.savefig(filename, bbox_inches='tight', dpi=300)