import requests
import json

url = 'https://apimedcab.herokuapp.com/api/'
#r = requests.post(url,json={"Depression and raspberry taste with citrus aroma"})
r = requests.post(url,json={query})


print(r.json())


