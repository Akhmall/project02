import requests

api_key = 'c7043f07-d22c-44cd-88b8-7216a8dcb503'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()
print(definitions)

for definition in definitions:
    print(definition)