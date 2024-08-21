import warnings
warnings.filterwarnings("ignore")

import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE)
response1 = requests.post(BASE)
response2 = requests.post(BASE + "sum", json={"num1": 4, "num2": 5})

print(response.json())
print(response1.json())
print(response2.json())