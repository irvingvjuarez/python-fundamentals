import requests
import json

URL_API = lambda name: f"https://api.nationalize.io?name={name}"

def get_country_code(name):
    res = requests.get(URL_API(name)).text
    print(res)

    country_code = json.loads(res)["country"][0]["country_id"]

    return country_code

if __name__ == "__main__":
    country_code = get_country_code("Irving")
    print(country_code)