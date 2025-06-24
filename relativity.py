# Physics/relativity.py

"""
Relativity Module
Implements Einstein's special relativity equations including time dilation,
length contraction, and mass-energy equivalence.
"""

from decimal import Decimal, getcontext
from Physics.constants import SPEED_OF_LIGHT

getcontext().prec = 50

def lorentz_factor(velocity: Decimal) -> Decimal:
    """Calculate Lorentz factor: γ = 1 / sqrt(1 - v²/c²)"""
    v2 = velocity ** 2
    c2 = SPEED_OF_LIGHT ** 2
    inside = Decimal("1") - (v2 / c2)
    if inside <= 0:
        raise ValueError("Velocity must be less than the speed of light")
    return Decimal("1") / inside.sqrt()

def time_dilation(proper_time: Decimal, velocity: Decimal) -> Decimal:
    """Calculate dilated time: t = γ * t₀"""
    γ = lorentz_factor(velocity)
    return γ * proper_time

def length_contraction(proper_length: Decimal, velocity: Decimal) -> Decimal:
    """Calculate contracted length: L = L₀ / γ"""
    γ = lorentz_factor(velocity)
    return proper_length / γ

def relativistic_mass(rest_mass: Decimal, velocity: Decimal) -> Decimal:
    """Calculate relativistic mass: m = γ * m₀"""
    γ = lorentz_factor(velocity)
    return γ * rest_mass

def mass_energy_equivalence(mass: Decimal) -> Decimal:
    """Calculate energy using E = mc²"""
    return mass * (SPEED_OF_LIGHT ** 2)

# Example usage
if __name__ == "__main__":
    v = Decimal("299000000")  # m/s
    t0 = Decimal("1.0")       # second

    print("Lorentz factor γ:", lorentz_factor(v))
    print("Time dilation at v=299,000,000 m/s:", time_dilation(t0, v), "s")
    print("Length contraction for 1m rod:", length_contraction(Decimal("1"), v), "m")
    print("Mass-energy of 1kg:", mass_energy_equivalence(Decimal("1")), "J")
