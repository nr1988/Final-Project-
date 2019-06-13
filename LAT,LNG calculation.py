import requests

address = "63321 North Tyler Avenue,El Monte,CA 91731"
api_key = "AIzaSyDF0GCwXjyQhr-Ayq8UKFa-ycO3elMO0xw"
api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
api_response_dict = api_response.json()

if api_response_dict['status'] == 'OK':
    latitude = api_response_dict['results'][0]['geometry']['location']['lat']
    longitude = api_response_dict['results'][0]['geometry']['location']['lng']
    print( 'Latitude:', latitude)
    print ('Longitude:', longitude)