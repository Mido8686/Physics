# Physics/fields.py

"""
Fields Module
Implements electric, gravitational, and magnetic field equations and forces.
"""

from decimal import Decimal, getcontext
from Physics.constants import GRAVITATIONAL_CONSTANT, ELEMENTARY_CHARGE, COULOMB_CONSTANT, MU_0, PI

getcontext().prec = 50

# Gravitational field: g = G * M / r²
def gravitational_field(mass: Decimal, distance: Decimal) -> Decimal:
    """Field strength (N/kg) at distance r from mass M"""
    return GRAVITATIONAL_CONSTANT * mass / distance**2

# Electric field: E = k * Q / r²
def electric_field(charge: Decimal, distance: Decimal) -> Decimal:
    """Electric field (N/C) from point charge at distance r"""
    return COULOMB_CONSTANT * charge / distance**2

# Magnetic field (infinite straight wire): B = μ₀ * I / (2πr)
def magnetic_field(current: Decimal, distance: Decimal) -> Decimal:
    """Magnetic field (Tesla) at distance r from wire carrying current I"""
    return MU_0 * current / (Decimal("2") * PI * distance)

# Gravitational potential energy: U = -G * m1 * m2 / r
def gravitational_potential_energy(m1: Decimal, m2: Decimal, r: Decimal) -> Decimal:
    return -GRAVITATIONAL_CONSTANT * m1 * m2 / r

# Electric potential energy: U = k * q1 * q2 / r
def electric_potential_energy(q1: Decimal, q2: Decimal, r: Decimal) -> Decimal:
    return COULOMB_CONSTANT * q1 * q2 / r

# Example usage
if __name__ == "__main__":
    M = Decimal("5.97e24")  # Earth mass in kg
    r = Decimal("6.371e6")  # Earth radius in m
    print("Gravitational field at Earth surface:", gravitational_field(M, r), "N/kg")

    Q = ELEMENTARY_CHARGE
    d = Decimal("0.01")  # 1 cm
    print("Electric field 1cm from 1e charge:", electric_field(Q, d), "N/C")

    I = Decimal("5.0")  # Amperes
    r_wire = Decimal("0.05")  # 5 cm
    print("Magnetic field near wire:", magnetic_field(I, r_wire), "T")
