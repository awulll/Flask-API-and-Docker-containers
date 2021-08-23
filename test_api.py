import requests
import json

# List of markets
markets = ['macapa','varejao']

# Inserting data for all markets
for market in markets:
    
    # Getting Json 
    data = json.load(open(f'js/contacts-{market}.json'))
    
    # Inserting json in the database
    res  = requests.post(f'http://localhost:5000/add_contact/{market}', json=data)
