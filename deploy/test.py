import requests

url = 'http://localhost:9696/predict'
data = {'img': ''}    
result = requests.post(url, files=data)
print(result)