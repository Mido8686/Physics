# Physics/electromagnetism.py

"""
Electromagnetism Module
Implements electric forces, fields, circuits, and magnetic principles using physical laws.
"""

from decimal import Decimal, getcontext
from Physics.constants import COULOMB_CONSTANT, ELEMENTARY_CHARGE, VACUUM_PERMITTIVITY

getcontext().prec = 50

# Coulomb's Law: F = k * q1 * q2 / r^2
def electric_force(q1: Decimal, q2: Decimal, distance: Decimal) -> Decimal:
    """Calculate electric force between two point charges (N)."""
    return COULOMB_CONSTANT * q1 * q2 / (distance ** 2)


# Electric field: E = F / q = k * Q / r^2
def electric_field(source_charge: Decimal, distance: Decimal) -> Decimal:
    """Calculate electric field (N/C)."""
    return COULOMB_CONSTANT * source_charge / (distance ** 2)


# Electric potential energy: U = k * q1 * q2 / r
def electric_potential_energy(q1: Decimal, q2: Decimal, distance: Decimal) -> Decimal:
    """Calculate electric potential energy (J)."""
    return COULOMB_CONSTANT * q1 * q2 / distance


# Electric potential (voltage): V = k * Q / r
def electric_potential(source_charge: Decimal, distance: Decimal) -> Decimal:
    """Calculate electric potential (V)."""
    return COULOMB_CONSTANT * source_charge / distance


# Capacitance of parallel plate: C = ε₀ * A / d
def capacitance(area: Decimal, distance: Decimal) -> Decimal:
    """Calculate capacitance (F)."""
    return VACUUM_PERMITTIVITY * area / distance


# Ohm's Law: V = IR
def voltage(current: Decimal, resistance: Decimal) -> Decimal:
    return current * resistance

def resistance(voltage: Decimal, current: Decimal) -> Decimal:
    return voltage / current

def current(voltage: Decimal, resistance: Decimal) -> Decimal:
    return voltage / resistance


# Power: P = IV = I^2 * R = V^2 / R
def electric_power(voltage: Decimal, current: Decimal) -> Decimal:
    return voltage * current


# Magnetic force: F = qvB sin(θ), assuming θ = 90°
def magnetic_force(charge: Decimal, velocity: Decimal, magnetic_field: Decimal) -> Decimal:
    """Calculate magnetic force (N)."""
    return charge * velocity * magnetic_field


# Example usage
if __name__ == "__main__":
    q1 = Decimal("1e-6")  # C
    q2 = Decimal("2e-6")  # C
    r = Decimal("0.05")   # m

    print("Electric force between q1 and q2:", electric_force(q1, q2, r), "N")
    print("Electric potential from q1 at 5cm:", electric_potential(q1, r), "V")
    
    A = Decimal("0.01")  # m²
    d = Decimal("0.001") # m
    print("Capacitance of parallel plates:", capacitance(A, d), "F")
