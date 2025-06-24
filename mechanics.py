# Physics/mechanics.py

"""
Classical Mechanics Module
Implements core laws of motion, force, energy, and gravity based on Newtonian physics.
"""

from decimal import Decimal
from Physics.constants import GRAVITATIONAL_CONSTANT, STANDARD_GRAVITY


# Newton's Second Law: F = ma
def force(mass: Decimal, acceleration: Decimal) -> Decimal:
    """Calculate force (N) given mass (kg) and acceleration (m/s^2)."""
    return mass * acceleration


# Acceleration: a = (v_final - v_initial) / t
def acceleration(v_final: Decimal, v_initial: Decimal, time: Decimal) -> Decimal:
    """Calculate acceleration (m/s^2) from change in velocity over time."""
    return (v_final - v_initial) / time


# Velocity: v = v_initial + at
def velocity(v_initial: Decimal, acceleration: Decimal, time: Decimal) -> Decimal:
    """Calculate final velocity (m/s)."""
    return v_initial + acceleration * time


# Displacement: s = v_initial * t + 0.5 * a * t^2
def displacement(v_initial: Decimal, acceleration: Decimal, time: Decimal) -> Decimal:
    """Calculate displacement (m)."""
    return v_initial * time + Decimal("0.5") * acceleration * (time ** 2)


# Kinetic Energy: KE = 0.5 * m * v^2
def kinetic_energy(mass: Decimal, velocity: Decimal) -> Decimal:
    """Calculate kinetic energy (J)."""
    return Decimal("0.5") * mass * (velocity ** 2)


# Potential Energy (gravitational): PE = m * g * h
def potential_energy(mass: Decimal, height: Decimal, gravity: Decimal = STANDARD_GRAVITY) -> Decimal:
    """Calculate gravitational potential energy (J)."""
    return mass * gravity * height


# Momentum: p = m * v
def momentum(mass: Decimal, velocity: Decimal) -> Decimal:
    """Calculate momentum (kg·m/s)."""
    return mass * velocity


# Gravitational Force: F = G * m1 * m2 / r^2
def gravitational_force(m1: Decimal, m2: Decimal, distance: Decimal) -> Decimal:
    """Calculate gravitational force between two masses (N)."""
    return GRAVITATIONAL_CONSTANT * m1 * m2 / (distance ** 2)


# Work: W = F * d
def work(force: Decimal, displacement: Decimal) -> Decimal:
    """Calculate work (J)."""
    return force * displacement


# Power: P = W / t
def power(work: Decimal, time: Decimal) -> Decimal:
    """Calculate power (W)."""
    return work / time


# Example usage
if __name__ == "__main__":
    m = Decimal("2.0")     # kg
    a = Decimal("3.0")     # m/s²
    h = Decimal("10")      # m
    v = Decimal("5.0")     # m/s

    print("Force:", force(m, a), "N")
    print("Kinetic Energy:", kinetic_energy(m, v), "J")
    print("Potential Energy:", potential_energy(m, h), "J")
