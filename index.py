from flask import Flask
import requests
app = Flask(__name__)
@app.route("/")
def main_page():
    return "Hello, this is the main page!, type country name after the '/'"

@app.route('/<name>')
def index(name):

    country = requests.get(f'https://restcountries.eu/rest/v2/name/{name}?fullText=true')
    print(country.status_code)
    if country.status_code == 200:
        print('You got the success!')
        name = country.json()[0]['name']
        capital = country.json()[0]['capital']
        language = country.json()[0]['languages'][0]['name']
        currency = country.json()[0]['currencies'][0]['name']
        currency_code = country.json()[0]['currencies'][0]['code']
        currency_rate = requests.get(
            f'http://data.fixer.io/api/latest?access_key=0f74f9e3e64cb0c2ce6ec5230dc7592d&format=1&symbols={currency_code}')
        if currency_rate.status_code == 200:
            print('You got the success!')
            rate = currency_rate.json()['rates'][f'{currency_code}']

    elif country.status_code == 404:
        print('Page not Found.')
        capital, language, currency, currency_code, rate = None, None, None, None, None
        return "COUNTRY NOT FOUND"
    return 'Country Name: %s capital City: %s language: %s currency: %s currency_code: %s rate: %s' % (name, capital, language, currency, currency_code, rate)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
