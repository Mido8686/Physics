# Physics/units.py

"""
Unit System and Conversion Tools
Supports metric SI units, scaling prefixes, and conversion between compatible types.
"""

from decimal import Decimal
from enum import Enum


# SI Prefixes (powers of ten)
SI_PREFIXES = {
    "y": Decimal("1e-24"),   # yocto
    "z": Decimal("1e-21"),   # zepto
    "a": Decimal("1e-18"),   # atto
    "f": Decimal("1e-15"),   # femto
    "p": Decimal("1e-12"),   # pico
    "n": Decimal("1e-9"),    # nano
    "u": Decimal("1e-6"),    # micro
    "m": Decimal("1e-3"),    # milli
    "":  Decimal("1e0"),     # base
    "k": Decimal("1e3"),     # kilo
    "M": Decimal("1e6"),     # mega
    "G": Decimal("1e9"),     # giga
    "T": Decimal("1e12"),    # tera
    "P": Decimal("1e15"),    # peta
    "E": Decimal("1e18"),    # exa
    "Z": Decimal("1e21"),    # zetta
    "Y": Decimal("1e24"),    # yotta
}


# Supported units (extendable)
class Unit(Enum):
    METER = "m"
    SECOND = "s"
    KILOGRAM = "kg"
    AMPERE = "A"
    KELVIN = "K"
    MOLE = "mol"
    CANDELA = "cd"
    NEWTON = "N"
    JOULE = "J"
    WATT = "W"
    HERTZ = "Hz"
    VOLT = "V"
    OHM = "Ω"
    COULOMB = "C"


def convert(value: Decimal, from_prefix: str, to_prefix: str) -> Decimal:
    """
    Convert a value from one SI prefix to another.
    Example: convert(Decimal('1.5'), 'k', '') => 1500 (kilo to base)
    """
    from_scale = SI_PREFIXES.get(from_prefix, Decimal("1"))
    to_scale = SI_PREFIXES.get(to_prefix, Decimal("1"))
    return value * (from_scale / to_scale)


def format_with_prefix(value: Decimal) -> str:
    """
    Automatically formats a number with an appropriate SI prefix.
    Example: 0.000001 becomes 1 μ
    """
    for prefix, scale in sorted(SI_PREFIXES.items(), key=lambda x: -x[1]):
        scaled = value / scale
        if Decimal("1") <= abs(scaled) < Decimal("1000"):
            return f"{scaled:.6g} {prefix}"
    return f"{value:.6g}"


# Example usage
if __name__ == "__main__":
    # Convert 1.5 kilometers to meters
    km_to_m = convert(Decimal("1.5"), "k", "")
    print(f"1.5 km = {km_to_m} m")

    # Format 0.000001 meters
    print(format_with_prefix(Decimal("0.000001")))
