# Lorenz Attractor Generator
Generates and visualizes the Lorenz attractor using matplotlib.

## Install

    pip install numpy matplotlib

## Usage

```python
import matplotlib.pyplot as plt
from lorenz_attractor import LorenzAttractor

attractor = LorenzAttractor(sigma=10, rho=28, beta=8/3)
attractor.generate()
attractor.visualize()
```

## Features

* Generate Lorenz attractor
* Visualize attractor using matplotlib
* Unit tests

## Files

* `lorenz_attractor.py` (main module)
* `test_lorenz_attractor.py` (unit test suite)
* `tests/` (test data and fixtures)

## Running Tests

    python -m unittest test_lorenz_attractor.py