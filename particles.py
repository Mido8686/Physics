# Physics/particles.py

"""
Particles Module
Models the Standard Model: quarks, leptons, bosons, and their basic properties.
"""

from dataclasses import dataclass
from decimal import Decimal
from typing import List

@dataclass
class Particle:
    name: str
    symbol: str
    mass: Decimal  # in kg
    charge: Decimal  # in Coulombs
    spin: Decimal  # in ℏ units
    type: str  # "fermion" or "boson"
    interactions: List[str]  # e.g., ["electromagnetic", "weak", "strong"]

# Constants
ELEMENTARY_CHARGE = Decimal("1.602176634e-19")

# Fundamental Fermions (12 total)
quarks = [
    Particle("Up quark", "u", Decimal("2.3e-30"), Decimal("2")/Decimal("3") * ELEMENTARY_CHARGE, Decimal("0.5"), "fermion", ["strong", "electromagnetic", "weak"]),
    Particle("Down quark", "d", Decimal("4.8e-30"), -Decimal("1")/Decimal("3") * ELEMENTARY_CHARGE, Decimal("0.5"), "fermion", ["strong", "electromagnetic", "weak"]),
    Particle("Charm quark", "c", Decimal("1.27e-27"), Decimal("2")/Decimal("3") * ELEMENTARY_CHARGE, Decimal("0.5"), "fermion", ["strong", "electromagnetic", "weak"]),
    Particle("Strange quark", "s", Decimal("9.5e-29"), -Decimal("1")/Decimal("3") * ELEMENTARY_CHARGE, Decimal("0.5"), "fermion", ["strong", "electromagnetic", "weak"]),
    Particle("Top quark", "t", Decimal("1.73e-24"), Decimal("2")/Decimal("3") * ELEMENTARY_CHARGE, Decimal("0.5"), "fermion", ["strong", "electromagnetic", "weak"]),
    Particle("Bottom quark", "b", Decimal("4.18e-27"), -Decimal("1")/Decimal("3") * ELEMENTARY_CHARGE, Decimal("0.5"), "fermion", ["strong", "electromagnetic", "weak"]),
]

leptons = [
    Particle("Electron", "e⁻", Decimal("9.10938356e-31"), -ELEMENTARY_CHARGE, Decimal("0.5"), "fermion", ["electromagnetic", "weak"]),
    Particle("Electron neutrino", "νₑ", Decimal("1e-36"), Decimal("0"), Decimal("0.5"), "fermion", ["weak"]),
    Particle("Muon", "μ⁻", Decimal("1.884e-28"), -ELEMENTARY_CHARGE, Decimal("0.5"), "fermion", ["electromagnetic", "weak"]),
    Particle("Muon neutrino", "ν_μ", Decimal("1e-36"), Decimal("0"), Decimal("0.5"), "fermion", ["weak"]),
    Particle("Tau", "τ⁻", Decimal("3.167e-27"), -ELEMENTARY_CHARGE, Decimal("0.5"), "fermion", ["electromagnetic", "weak"]),
    Particle("Tau neutrino", "ν_τ", Decimal("1e-36"), Decimal("0"), Decimal("0.5"), "fermion", ["weak"]),
]

# Bosons
bosons = [
    Particle("Photon", "γ", Decimal("0"), Decimal("0"), Decimal("1"), "boson", ["electromagnetic"]),
    Particle("Gluon", "g", Decimal("0"), Decimal("0"), Decimal("1"), "boson", ["strong"]),
    Particle("W boson", "W±", Decimal("1.434e-25"), ±ELEMENTARY_CHARGE, Decimal("1"), "boson", ["weak"]),
    Particle("Z boson", "Z⁰", Decimal("1.629e-25"), Decimal("0"), Decimal("1"), "boson", ["weak"]),
    Particle("Higgs boson", "H⁰", Decimal("2.246e-25"), Decimal("0"), Decimal("0"), "boson", ["weak"]),
    Particle("Graviton", "G?", Decimal("0"), Decimal("0"), Decimal("2"), "boson", ["gravitational"]),  # Theoretical
]

# Particle lookup
standard_model = {p.symbol: p for p in quarks + leptons + bosons}

# Example function: get antiparticle
def get_antiparticle(p: Particle) -> Particle:
    return Particle(
        name=f"Anti-{p.name}",
        symbol=p.symbol.replace("⁻", "+").replace("ν", "anti-ν"),
        mass=p.mass,
        charge=-p.charge,
        spin=p.spin,
        type=p.type,
        interactions=p.interactions,
    )

# Example usage
if __name__ == "__main__":
    e = standard_model["e⁻"]
    anti_e = get_antiparticle(e)
    print("Electron:", e)
    print("Positron:", anti_e)

    u = standard_model["u"]
    print("Up Quark:", u.name, "Charge:", u.charge / ELEMENTARY_CHARGE, "e")
