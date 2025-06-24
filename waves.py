# Physics/waves.py

"""
General Wave Physics Module
Covers the base properties of waves: harmonic motion, interference, and wave behavior.
"""

from decimal import Decimal, getcontext
from math import sin, pi

getcontext().prec = 50

# Wave equation: v = f * λ (reused from sound.py if needed)

def wave_function(amplitude: Decimal, frequency: Decimal, time: Decimal, phase: Decimal = Decimal("0")) -> Decimal:
    """
    Basic wave function: y(t) = A * sin(2πft + φ)
    """
    return amplitude * Decimal(sin(float(2 * pi * frequency * time + phase)))


def angular_frequency(frequency: Decimal) -> Decimal:
    """ω = 2πf"""
    return Decimal("2") * Decimal(pi) * frequency


def harmonic_frequency(fundamental_freq: Decimal, harmonic_number: int) -> Decimal:
    """Calculate frequency of nth harmonic."""
    return fundamental_freq * Decimal(harmonic_number)


def standing_wave_length(length: Decimal, harmonic_number: int, fixed_ends: bool = True) -> Decimal:
    """
    Standing wave wavelength based on harmonic number.
    For string with both ends fixed: λ = 2L / n
    """
    if fixed_ends:
        return Decimal("2") * length / Decimal(harmonic_number)
    else:
        # One end fixed (like open pipe): λ = 4L / (2n - 1)
        return Decimal("4") * length / Decimal(2 * harmonic_number - 1)


def superposition(wave1: Decimal, wave2: Decimal) -> Decimal:
    """Add two wave amplitudes (constructive/destructive interference)."""
    return wave1 + wave2


def beat_frequency(f1: Decimal, f2: Decimal) -> Decimal:
    """Calculate beat frequency: |f1 - f2|"""
    return abs(f1 - f2)


def reflection_phase_change(fixed_end: bool) -> str:
    """
    Describes phase change due to reflection.
    Fixed end → 180° (π) phase shift.
    Free end → no phase shift.
    """
    return "π (180°)" if fixed_end else "0 (no phase shift)"


# Example usage
if __name__ == "__main__":
    A = Decimal("1.0")
    f = Decimal("10")
    t = Decimal("0.1")
    y = wave_function(A, f, t)
    print(f"Wave displacement at t={t}s: {y} units")

    print("2nd harmonic frequency of 100Hz fundamental:", harmonic_frequency(Decimal("100"), 2), "Hz")
    print("Standing wavelength for L=1m, n=2:", standing_wave_length(Decimal("1"), 2), "m")
    print("Beat frequency between 440Hz and 445Hz:", beat_frequency(Decimal("440"), Decimal("445")), "Hz")
