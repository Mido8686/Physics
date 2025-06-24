# Physics/thermodynamics.py

"""
Thermodynamics Module
Implements heat, temperature, energy transfer, and entropy according to classical thermodynamics.
"""

from decimal import Decimal, getcontext
from Physics.constants import BOLTZMANN_CONSTANT

getcontext().prec = 50

# Temperature conversion
def celsius_to_kelvin(temp_c: Decimal) -> Decimal:
    return temp_c + Decimal("273.15")

def kelvin_to_celsius(temp_k: Decimal) -> Decimal:
    return temp_k - Decimal("273.15")

def fahrenheit_to_celsius(temp_f: Decimal) -> Decimal:
    return (temp_f - Decimal("32")) * Decimal("5") / Decimal("9")

def celsius_to_fahrenheit(temp_c: Decimal) -> Decimal:
    return (temp_c * Decimal("9") / Decimal("5")) + Decimal("32")


# Heat transfer: Q = mcΔT
def heat_transfer(mass: Decimal, specific_heat: Decimal, delta_temp: Decimal) -> Decimal:
    """Calculate heat energy (J)."""
    return mass * specific_heat * delta_temp


# Ideal gas law: PV = nRT
def ideal_gas_pressure(n_moles: Decimal, temperature: Decimal, volume: Decimal, R: Decimal = Decimal("8.314")) -> Decimal:
    """Calculate pressure (Pa) from ideal gas law."""
    return n_moles * R * temperature / volume


# First Law of Thermodynamics: ΔU = Q - W
def change_internal_energy(heat_added: Decimal, work_done: Decimal) -> Decimal:
    """Calculate internal energy change (J)."""
    return heat_added - work_done


# Entropy change: ΔS = Q / T (reversible)
def entropy_change(heat: Decimal, temperature: Decimal) -> Decimal:
    """Calculate change in entropy (J/K)."""
    return heat / temperature


# Efficiency of heat engine: η = 1 - Tc/Th
def carnot_efficiency(temp_hot: Decimal, temp_cold: Decimal) -> Decimal:
    """Calculate maximum theoretical efficiency."""
    return Decimal("1") - (temp_cold / temp_hot)


# Example usage
if __name__ == "__main__":
    m = Decimal("2.0")  # kg
    c = Decimal("4186")  # J/kg·K for water
    dT = Decimal("20")

    Q = heat_transfer(m, c, dT)
    print("Heat transferred to 2kg water by 20°C:", Q, "J")

    U = change_internal_energy(Q, Decimal("1000"))
    print("Internal energy change (Q - W):", U, "J")

    S = entropy_change(Q, celsius_to_kelvin(Decimal("25")))
    print("Entropy change:", S, "J/K")
