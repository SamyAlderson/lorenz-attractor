# tests/test_lorenz.py

import unittest
import numpy as np
from src.lorenz import LorenzAttractor

class TestLorenzAttractor(unittest.TestCase):
    def test_sanity(self):
        # Basic sanity check to ensure the attractor is generated correctly
        attractor = LorenzAttractor(sigma=10, rho=28, beta=8/3)
        x, y, z = attractor.solve(1000)
        self.assertGreaterEqual(len(x), 1000)

    def test_sigma(self):
        # Test the effect of sigma on the attractor
        attractor1 = LorenzAttractor(sigma=10, rho=28, beta=8/3)
        attractor2 = LorenzAttractor(sigma=5, rho=28, beta=8/3)
        x1, y1, z1 = attractor1.solve(1000)
        x2, y2, z2 = attractor2.solve(1000)
        # Not proud of this but it works
        self.assertNotAlmostEqual(np.mean(x1), np.mean(x2), places=2)

    def test_rho(self):
        # Test the effect of rho on the attractor
        attractor1 = LorenzAttractor(sigma=10, rho=30, beta=8/3)
        attractor2 = LorenzAttractor(sigma=10, rho=25, beta=8/3)
        x1, y1, z1 = attractor1.solve(1000)
        x2, y2, z2 = attractor2.solve(1000)
        # This was tricky
        self.assertNotAlmostEqual(np.mean(y1), np.mean(y2), places=2)

    def test_beta(self):
        # Test the effect of beta on the attractor
        attractor1 = LorenzAttractor(sigma=10, rho=28, beta=10/3)
        attractor2 = LorenzAttractor(sigma=10, rho=28, beta=6/3)
        x1, y1, z1 = attractor1.solve(1000)
        x2, y2, z2 = attractor2.solve(1000)
        # Not proud of this but it works
        self.assertNotAlmostEqual(np.mean(z1), np.mean(z2), places=2)

if __name__ == '__main__':
    unittest.main()