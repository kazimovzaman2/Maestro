import requests

endpoint = "http://localhost:8000/api/products/1117178787171916156135119/"

get_response = requests.get(endpoint)
print(get_response.json())