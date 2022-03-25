import requests
import json



data = dict()

data["completed"] = 1
response = requests.post(
    'https://notes-backend-flutter.herokuapp.com/notes/98', 
    data=data)


print(response.text)