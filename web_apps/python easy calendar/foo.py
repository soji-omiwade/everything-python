import requests
response = requests.get(


    url='GET https://www.googleapis.com/calendar/v3/calendars/omiwade@gmail.com',
    headers={'Authorization': 'Bearer ACCESS_TOKEN'},
)
response.raise_for_status()
calendars = response.json().get('items')