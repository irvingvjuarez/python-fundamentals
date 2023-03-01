from typing import Dict, List

positives: List[int] = ["h", "e", "l", "l", "o"]

users: Dict[str, int] = {
    "argentina": 21,
    "mexico": 81,
    "brasil": 42
}

countries: List[Dict[str, str]] = [
    {
        "name": "Argentina",
        "people": "27633"
    },
    {
        "name": "México",
        "people": "255142"
    },
    {
        "name": "Brasil",
        "people": "8725263"
    }
]

print(positives)
print(users)
print(countries)
