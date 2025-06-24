# Physics/optics.py

"""
Optics Module
Implements physics of light, lenses, mirrors, reflection, and refraction.
"""

from decimal import Decimal, getcontext
from Physics.constants import SPEED_OF_LIGHT

getcontext().prec = 50

# Reflection: angle of incidence = angle of reflection (simple rule-based, no math needed)

# Snell's Law: n1 * sin(θ1) = n2 * sin(θ2)
def snells_law(n1: Decimal, theta1_deg: Decimal, n2: Decimal) -> Decimal:
    """Calculate angle of refraction in degrees."""
    import math
    theta1_rad = math.radians(float(theta1_deg))
    sin_theta2 = (n1 / n2) * Decimal(math.sin(theta1_rad))
    if sin_theta2 > 1:
        raise ValueError("Total internal reflection (no refraction)")
    theta2_rad = math.asin(float(sin_theta2))
    return Decimal(math.degrees(theta2_rad))

# Lens & mirror equation: 1/f = 1/do + 1/di
def image_distance(focal_length: Decimal, object_distance: Decimal) -> Decimal:
    """Calculate image distance using lens/mirror equation."""
    return Decimal("1") / (Decimal("1") / focal_length - Decimal("1") / object_distance)

# Magnification: m = -di / do (mirrors), m = +di / do (lenses)
def magnification(image_distance: Decimal, object_distance: Decimal, is_mirror: bool = False) -> Decimal:
    """Calculate magnification of image."""
    if is_mirror:
        return -image_distance / object_distance
    return image_distance / object_distance

# Speed of light in medium: v = c / n
def speed_in_medium(refractive_index: Decimal) -> Decimal:
    return SPEED_OF_LIGHT / refractive_index

# Focal length from radius of curvature: f = R / 2
def focal_length_from_radius(radius_of_curvature: Decimal) -> Decimal:
    return radius_of_curvature / 2

# Example usage
if __name__ == "__main__":
    # Refraction: air to glass
    n_air = Decimal("1.0")
    n_glass = Decimal("1.5")
    angle_incident = Decimal("30")
    angle_refracted = snells_law(n_air, angle_incident, n_glass)
    print("Refracted angle in glass:", angle_refracted, "degrees")

    # Lens image
    f = Decimal("0.1")   # 10 cm lens
    do = Decimal("0.2")  # 20 cm object
    di = image_distance(f, do)
    m = magnification(di, do)
    print("Image distance:", di, "m")
    print("Magnification:", m)

    # Light speed in water (n=1.33)
    print("Speed of light in water:", speed_in_medium(Decimal("1.33")), "m/s")
