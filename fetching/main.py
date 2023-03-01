import requests

URL_API = lambda name: f"https://api.nationalize.io?name={name}"

def get_country_code(name):
    res = requests.get(URL_API(name)).json()
    country_code = res["country"][0]["country_id"]

    return country_code

if __name__ == "__main__":
    country_code = get_country_code("Irving")
    print(country_code)