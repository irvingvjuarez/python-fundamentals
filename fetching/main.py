import requests

URL_API = "https://api.nationalize.io?name=michael"

def main():
    r = requests.get(URL_API).json()
    print(r)

if __name__ == "__main__":
    main()