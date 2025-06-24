# Physics/astrophysics.py

"""
Astrophysics Module
Implements gravity, orbital mechanics, black holes, and cosmic expansion.
"""

from decimal import Decimal, getcontext
from Physics.constants import GRAVITATIONAL_CONSTANT, SPEED_OF_LIGHT, HUBBLE_CONSTANT, PI

getcontext().prec = 50

# Newton's Law of Gravitation: F = G * m1 * m2 / r²
def gravitational_force(m1: Decimal, m2: Decimal, r: Decimal) -> Decimal:
    """Gravitational force between two masses."""
    return GRAVITATIONAL_CONSTANT * m1 * m2 / r**2

# Orbital velocity: v = √(G * M / r)
def orbital_velocity(mass_central: Decimal, orbital_radius: Decimal) -> Decimal:
    """Velocity of satellite in circular orbit."""
    return (GRAVITATIONAL_CONSTANT * mass_central / orbital_radius).sqrt()

# Escape velocity: v = √(2 * G * M / r)
def escape_velocity(mass: Decimal, radius: Decimal) -> Decimal:
    return (Decimal("2") * GRAVITATIONAL_CONSTANT * mass / radius).sqrt()

# Kepler's Third Law: T² = (4π² * r³) / (G * M)
def orbital_period(mass_central: Decimal, radius: Decimal) -> Decimal:
    numerator = Decimal("4") * PI**2 * radius**3
    denominator = GRAVITATIONAL_CONSTANT * mass_central
    return (numerator / denominator).sqrt()

# Schwarzschild radius: R = 2GM / c²
def schwarzschild_radius(mass: Decimal) -> Decimal:
    return Decimal("2") * GRAVITATIONAL_CONSTANT * mass / SPEED_OF_LIGHT**2

# Hubble's Law: v = H₀ * d
def recessional_velocity(distance_mpc: Decimal) -> Decimal:
    """Recessional velocity in m/s for a given distance in Megaparsecs."""
    return HUBBLE_CONSTANT * distance_mpc

# Example usage
if __name__ == "__main__":
    earth_mass = Decimal("5.97e24")
    earth_radius = Decimal("6.371e6")
    sat_altitude = Decimal("4.22e7")

    print("Gravitational force Earth–Moon:", gravitational_force(earth_mass, Decimal("7.35e22"), Decimal("3.84e8")), "N")
    print("Orbital velocity at 42,200 km:", orbital_velocity(earth_mass, sat_altitude), "m/s")
    print("Escape velocity from Earth:", escape_velocity(earth_mass, earth_radius), "m/s")
    print("Schwarzschild radius of Sun:", schwarzschild_radius(Decimal("1.989e30")), "m")
    print("Recessional velocity at 100 Mpc:", recessional_velocity(Decimal("100")), "m/s")
