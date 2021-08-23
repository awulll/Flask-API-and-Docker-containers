from flask import Flask,request,render_template,jsonify,session,make_response
from send_data import format_values,c_engine,insert,config,test_phone,test_name
import jwt
from datetime import *

# Creating app
app = Flask('Mercafacil')
valid_markets = ['macapa', 'varejao']

# Route for insert contacts    
@app.route('/add_contact/<market>', methods=['POST'])
def add_contact(market):
    
    # Test for market name    
    if market in valid_markets:
        
        # Choosing database acording market
        engine     = c_engine(market,config)
        connection = engine.connect()
        
        # Getting content
        content    = request.json
        for contacts in content: 
            for contact in content[contacts]:
                
                # Testing input data
                phone = test_phone(contact['cellphone'])
                name  = test_name(contact['name'],market,config)
                
                # Inserting if input is ok
                if None not in (name,phone):
                    n,c = format_values({'name':name,'cellphone':phone},market)
                    insert(connection,market,n,c)
                else: 
                    print ('Invalid input(s):',contact)
                    continue
                
        return '0'
    else:
        print ('Invalid market:',market) 
        return '1'   

app.run(debug=True)
