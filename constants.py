# Physics/constants.py

"""
Universal Physical Constants
These values are based on CODATA 2018 recommended values.
"""

from decimal import Decimal, getcontext

# Set precision for Decimal operations
getcontext().prec = 50

# Fundamental constants
SPEED_OF_LIGHT = Decimal("299792458")             # m/s
PLANCK_CONSTANT = Decimal("6.62607015e-34")        # J·s
REDUCED_PLANCK = PLANCK_CONSTANT / (2 * Decimal("3.141592653589793"))
GRAVITATIONAL_CONSTANT = Decimal("6.67430e-11")    # m³/kg/s²
ELEMENTARY_CHARGE = Decimal("1.602176634e-19")     # C
AVOGADRO_NUMBER = Decimal("6.02214076e23")         # mol⁻¹
BOLTZMANN_CONSTANT = Decimal("1.380649e-23")       # J/K
GAS_CONSTANT = Decimal("8.314462618")              # J/mol/K
ELECTRON_MASS = Decimal("9.10938356e-31")          # kg
PROTON_MASS = Decimal("1.67262192369e-27")         # kg
NEUTRON_MASS = Decimal("1.67492749804e-27")        # kg
PLANETARY_MASS_EARTH = Decimal("5.972e24")         # kg
PLANETARY_RADIUS_EARTH = Decimal("6371000")        # m

# Derived constants
LIGHT_YEAR = SPEED_OF_LIGHT * Decimal("31557600")  # meters in one Julian year
STANDARD_GRAVITY = Decimal("9.80665")              # m/s²

# Temperature conversions
ABSOLUTE_ZERO_C = Decimal("-273.15")               # °C
