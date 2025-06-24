# Physics/quantum.py

"""
Quantum Physics Module
Implements key quantum principles: quantization, uncertainty, wave-particle duality.
"""

from decimal import Decimal, getcontext
from Physics.constants import PLANCK_CONSTANT, SPEED_OF_LIGHT

getcontext().prec = 50

# Planck's relation: E = h * f
def energy_from_frequency(frequency: Decimal) -> Decimal:
    """Calculate photon energy (Joules) from frequency."""
    return PLANCK_CONSTANT * frequency

# E = hc / λ
def energy_from_wavelength(wavelength: Decimal) -> Decimal:
    """Calculate photon energy (Joules) from wavelength (meters)."""
    return PLANCK_CONSTANT * SPEED_OF_LIGHT / wavelength

# De Broglie wavelength: λ = h / p
def de_broglie_wavelength(mass: Decimal, velocity: Decimal) -> Decimal:
    """Calculate wavelength of a particle."""
    momentum = mass * velocity
    return PLANCK_CONSTANT / momentum

# Heisenberg uncertainty principle: Δx * Δp ≥ ħ / 2
def uncertainty_position(momentum_uncertainty: Decimal) -> Decimal:
    """Estimate position uncertainty given Δp."""
    h_bar = PLANCK_CONSTANT / (Decimal("2") * Decimal("3.141592653589793"))
    return h_bar / (Decimal("2") * momentum_uncertainty)

def uncertainty_momentum(position_uncertainty: Decimal) -> Decimal:
    """Estimate momentum uncertainty given Δx."""
    h_bar = PLANCK_CONSTANT / (Decimal("2") * Decimal("3.141592653589793"))
    return h_bar / (Decimal("2") * position_uncertainty)

# Energy levels of hydrogen: E_n = -13.6 eV / n² (converted to Joules)
def hydrogen_energy_level(n: int) -> Decimal:
    """Energy of electron at quantum level n in hydrogen atom (Joules)."""
    eV_to_Joule = Decimal("1.602176634e-19")
    return -Decimal("13.6") * eV_to_Joule / Decimal(n**2)

# Example usage
if __name__ == "__main__":
    f = Decimal("5e14")  # Hz
    print("Photon energy for 5e14 Hz:", energy_from_frequency(f), "J")

    λ = Decimal("500e-9")  # m
    print("Photon energy for 500nm light:", energy_from_wavelength(λ), "J")

    m = Decimal("9.11e-31")  # kg (electron)
    v = Decimal("1e6")       # m/s
    print("De Broglie wavelength of electron:", de_broglie_wavelength(m, v), "m")

    dp = Decimal("1e-24")
    print("Uncertainty in position:", uncertainty_position(dp), "m")

    print("Hydrogen energy at n=2:", hydrogen_energy_level(2), "J")
