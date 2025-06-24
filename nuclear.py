# Physics/nuclear.py

"""
Nuclear Physics Module
Implements radioactive decay, nuclear reactions, mass defect, and nuclear energy.
"""

from decimal import Decimal, getcontext
from Physics.constants import SPEED_OF_LIGHT

getcontext().prec = 50

LN2 = Decimal("0.6931471805599453")

# Mass defect: Δm = (Z * m_p + N * m_n) - m_nucleus
def mass_defect(protons: Decimal, neutrons: Decimal, nucleus_mass: Decimal, proton_mass: Decimal, neutron_mass: Decimal) -> Decimal:
    """Calculate mass defect (kg)."""
    return (protons * proton_mass + neutrons * neutron_mass) - nucleus_mass

# Nuclear binding energy: E = Δm * c²
def binding_energy(mass_defect: Decimal) -> Decimal:
    """Calculate binding energy (Joules)."""
    return mass_defect * SPEED_OF_LIGHT ** 2

# Radioactive decay: N(t) = N₀ * e^(-λt)
def radioactive_decay(N0: Decimal, decay_constant: Decimal, time: Decimal) -> Decimal:
    """Calculate undecayed nuclei at time t."""
    exponent = -decay_constant * time
    return N0 * exponent.exp()

# Half-life: T₁/₂ = ln(2) / λ
def half_life(decay_constant: Decimal) -> Decimal:
    return LN2 / decay_constant

# Decay constant: λ = ln(2) / T₁/₂
def decay_constant_from_half_life(half_life: Decimal) -> Decimal:
    return LN2 / half_life

# Fusion energy: E = Δm * c² (same as binding_energy)
def fusion_energy(initial_mass: Decimal, final_mass: Decimal) -> Decimal:
    """Energy released during nuclear fusion."""
    Δm = initial_mass - final_mass
    return Δm * SPEED_OF_LIGHT ** 2

# Fission energy: use same function, just with mass loss during fission
def fission_energy(initial_mass: Decimal, fragment_masses: list[Decimal]) -> Decimal:
    """Energy released during nuclear fission."""
    final_mass = sum(fragment_masses)
    Δm = initial_mass - final_mass
    return Δm * SPEED_OF_LIGHT ** 2

# Example usage
if __name__ == "__main__":
    # Example: Uranium-235 fission
    U_mass = Decimal("3.902e-25")  # kg
    fission_products = [Decimal("1.5e-25"), Decimal("2.3e-25")]
    E_fission = fission_energy(U_mass, fission_products)
    print("Energy released by U-235 fission:", E_fission, "J")

    # Radioactive decay
    N0 = Decimal("1e6")
    T_half = Decimal("5730")  # years, Carbon-14
    λ = decay_constant_from_half_life(T_half)
    N_t = radioactive_decay(N0, λ, Decimal("10000"))
    print("Remaining nuclei after 10,000 years:", N_t)

    # Mass defect of helium-4
    Z = Decimal("2")
    N = Decimal("2")
    m_p = Decimal("1.6726219e-27")
    m_n = Decimal("1.6749275e-27")
    m_He = Decimal("6.646478e-27")
    Δm = mass_defect(Z, N, m_He, m_p, m_n)
    E_bind = binding_energy(Δm)
    print("Binding energy of helium-4:", E_bind, "J")
