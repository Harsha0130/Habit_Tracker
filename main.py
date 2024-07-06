import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "aebe924sdvadsom",
    "username": "harshahmm",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
    "thanksCode": "Thank you!",
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)
