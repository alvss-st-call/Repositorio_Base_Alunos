import requests

id = 0

for id in  range(100,200):
    url= (f"https://68641b8088359a373e978349.mockapi.io/produto/{id}")

    response = requests.delete(url)

    print(response.status_code)
    print(response.text)