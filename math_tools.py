# Physics/math_tools.py

"""
Math Tools Module
Provides vector and matrix operations, integration, and tensor placeholders.
"""

from decimal import Decimal
from typing import List

# Vector operations
def vector_add(v1: List[Decimal], v2: List[Decimal]) -> List[Decimal]:
    return [a + b for a, b in zip(v1, v2)]

def dot_product(v1: List[Decimal], v2: List[Decimal]) -> Decimal:
    return sum(a * b for a, b in zip(v1, v2))

def cross_product(v1: List[Decimal], v2: List[Decimal]) -> List[Decimal]:
    return [
        v1[1]*v2[2] - v1[2]*v2[1],
        v1[2]*v2[0] - v1[0]*v2[2],
        v1[0]*v2[1] - v1[1]*v2[0]
    ]

# Matrix multiplication
def matrix_multiply(A: List[List[Decimal]], B: List[List[Decimal]]) -> List[List[Decimal]]:
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            val = sum(A[i][k] * B[k][j] for k in range(len(B)))
            row.append(val)
        result.append(row)
    return result

# Numerical integration (trapezoidal rule)
def trapezoidal_integrate(x: List[Decimal], y: List[Decimal]) -> Decimal:
    integral = Decimal("0")
    for i in range(1, len(x)):
        dx = x[i] - x[i - 1]
        avg_y = (y[i] + y[i - 1]) / Decimal("2")
        integral += dx * avg_y
    return integral

# Tensor stub (symbolic tensor representation)
class Tensor:
    def __init__(self, rank: int, components: List):
        self.rank = rank
        self.components = components

    def __repr__(self):
        return f"Tensor(rank={self.rank}, components={self.components})"

# Example usage
if __name__ == "__main__":
    v1 = [Decimal("1"), Decimal("2"), Decimal("3")]
    v2 = [Decimal("4"), Decimal("5"), Decimal("6")]

    print("Dot Product:", dot_product(v1, v2))
    print("Cross Product:", cross_product(v1, v2))
    print("Vector Add:", vector_add(v1, v2))

    A = [
        [Decimal("1"), Decimal("2")],
        [Decimal("3"), Decimal("4")]
    ]
    B = [
        [Decimal("2"), Decimal("0")],
        [Decimal("1"), Decimal("2")]
    ]
    print("Matrix Multiply:", matrix_multiply(A, B))

    x_vals = [Decimal("0"), Decimal("1"), Decimal("2")]
    y_vals = [Decimal("0"), Decimal("1"), Decimal("4")]
    print("Trapezoidal Integral:", trapezoidal_integrate(x_vals, y_vals))
