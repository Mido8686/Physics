# Physics/sound.py

"""
Sound Physics Module
Models the physics of real sound: waves, frequency, speed, and the Doppler effect.
"""

from decimal import Decimal, getcontext
from Physics.constants import STANDARD_GRAVITY

getcontext().prec = 50

# Speed of sound in various media (approximate, 20°C)
SPEED_OF_SOUND_AIR = Decimal("343")         # m/s
SPEED_OF_SOUND_WATER = Decimal("1482")      # m/s
SPEED_OF_SOUND_STEEL = Decimal("5960")      # m/s

# Wave equation: v = f * λ
def wave_speed(frequency: Decimal, wavelength: Decimal) -> Decimal:
    """Calculate wave speed (m/s)."""
    return frequency * wavelength

def wavelength(speed: Decimal, frequency: Decimal) -> Decimal:
    """Calculate wavelength (m) from speed and frequency."""
    return speed / frequency

def frequency(speed: Decimal, wavelength: Decimal) -> Decimal:
    """Calculate frequency (Hz)."""
    return speed / wavelength

def period(frequency: Decimal) -> Decimal:
    """Calculate wave period (s)."""
    return Decimal("1") / frequency


# Doppler effect for moving source and/or observer (air medium)
def doppler_effect(
    source_freq: Decimal,
    source_speed: Decimal,
    observer_speed: Decimal,
    wave_speed: Decimal = SPEED_OF_SOUND_AIR
) -> Decimal:
    """
    Calculate the observed frequency using the Doppler effect.
    Positive speeds = moving toward the other object.
    
    f' = f * (v + v_o) / (v - v_s)
    """
    return source_freq * ((wave_speed + observer_speed) / (wave_speed - source_speed))


# Sound Intensity: I = P / (4πr²)
def intensity(power: Decimal, distance: Decimal) -> Decimal:
    """Calculate sound intensity (W/m²)."""
    pi = Decimal("3.141592653589793")
    return power / (Decimal("4") * pi * (distance ** 2))


# Sound Level in decibels: L = 10 * log10(I / I₀)
def sound_level_db(intensity: Decimal, ref_intensity: Decimal = Decimal("1e-12")) -> Decimal:
    """Calculate sound level in decibels (dB)."""
    from math import log10
    ratio = float(intensity / ref_intensity)
    return Decimal(10 * log10(ratio))


# Example usage
if __name__ == "__main__":
    f = Decimal("440")  # Hz (A4 pitch)
    v = SPEED_OF_SOUND_AIR
    λ = wavelength(v, f)

    print("Wavelength of 440 Hz in air:", λ, "m")

    # Doppler effect: source moving toward observer at 30 m/s
    obs_freq = doppler_effect(f, Decimal("30"), Decimal("0"))
    print("Observed frequency (source approaching at 30 m/s):", obs_freq, "Hz")
