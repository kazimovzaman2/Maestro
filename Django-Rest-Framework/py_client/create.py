import requests


headers = {'Authorization': 'Bearer d212e28cb3835f557b4fe0e2e09ee151b205321a'}
endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "This field is done.",
    "price": 32.99
}

get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())