import requests
from datetime import datetime

TOKEN = "aebe924sdvadsom"
USERNAME = "harshahmm"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

header = {
    "X-USER-TOKEN": TOKEN
}
GRAPH_ID = "graph1"
graph_config = {
    "id": GRAPH_ID,
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime(year=2024, month=7, day=6)

pixel_creation_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "6",
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_creation_params, headers=header)
# print(response.text)


# *****************************************PUT*****************************************
update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{pixel_creation_params["date"]}"

pixel_update_params = {
    "quantity": "8"
}

response = requests.put(url=update_pixel_endpoint, json=pixel_update_params, headers=header)
print(response.text)


