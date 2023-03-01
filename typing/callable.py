from typing import Callable
import requests

def callback(res: str) -> str:
    return f"Your api response is \n {res}"

def fetch_data(api: str, cb: Callable[[str], str]) -> str:
    res = requests.get(api).text
    return cb(res)

if __name__ == "__main__":
    api_res = fetch_data("https://pokeapi.co/api/v2/pokemon/ditto", callback)
    print(api_res)