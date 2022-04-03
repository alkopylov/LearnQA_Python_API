import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
first_response = response.history[0]
last_response = response
print(response.history)
print(last_response.url)
print (last_response.status_code)
