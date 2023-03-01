from typing import List

Vector = List[float]

def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

if __name__ == "__main__":
    new_vector = [0.4, 2.1, 8.3, 4.2, 0.9, 12.7]
    print( scale(1.2, new_vector) )