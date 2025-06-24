# Physics/chaos.py

"""
Chaos Module
Models deterministic chaos and nonlinear systems: Lorenz system, logistic map.
"""

from typing import List, Tuple
from decimal import Decimal, getcontext

getcontext().prec = 50

# Lorenz system: dx/dt = σ(y - x), dy/dt = x(ρ - z) - y, dz/dt = xy - βz
def lorenz_step(x: Decimal, y: Decimal, z: Decimal, sigma: Decimal, rho: Decimal, beta: Decimal, dt: Decimal) -> Tuple[Decimal, Decimal, Decimal]:
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    x_new = x + dx * dt
    y_new = y + dy * dt
    z_new = z + dz * dt
    return x_new, y_new, z_new

def lorenz_trajectory(x0: Decimal, y0: Decimal, z0: Decimal, sigma: Decimal, rho: Decimal, beta: Decimal, dt: Decimal, steps: int) -> List[Tuple[Decimal, Decimal, Decimal]]:
    trajectory = []
    x, y, z = x0, y0, z0
    for _ in range(steps):
        x, y, z = lorenz_step(x, y, z, sigma, rho, beta, dt)
        trajectory.append((x, y, z))
    return trajectory

# Logistic map: x_{n+1} = r * x_n * (1 - x_n)
def logistic_map(r: Decimal, x0: Decimal, steps: int) -> List[Decimal]:
    results = []
    x = x0
    for _ in range(steps):
        x = r * x * (Decimal("1") - x)
        results.append(x)
    return results

# Example usage
if __name__ == "__main__":
    sigma = Decimal("10")
    rho = Decimal("28")
    beta = Decimal("8") / Decimal("3")
    dt = Decimal("0.01")
    steps = 100

    print("Lorenz Attractor Trajectory (First 5 points):")
    traj = lorenz_trajectory(Decimal("1"), Decimal("1"), Decimal("1"), sigma, rho, beta, dt, steps)
    for point in traj[:5]:
        print(point)

    print("\nLogistic Map (r=3.7, x0=0.5):")
    logistic = logistic_map(Decimal("3.7"), Decimal("0.5"), 20)
    for i, x in enumerate(logistic):
        print(f"Step {i}: {x}")
