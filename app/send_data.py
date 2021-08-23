import sqlalchemy as db
import json
import unidecode

# Parameters
config  = {'macapa': {'host':'localhost',
                      'port':3306,
                      'user':'admin',
                      'password':'admin',
                      'database':'admin',
                      'sizename':200},
           'varejao':{'host':'localhost',
                      'port':5432,
                      'user':'admin',
                      'password':'admin',
                      'database':'admin',
                      'sizename':100}}

# Format values for each database format
def format_values(contact,database):
    if database == 'macapa':
        name      = unidecode.unidecode(contact['name']).upper().strip()
        v         = contact['cellphone'].strip()
        cod       = v[:2]
        ddd       = v[2:4]
        pre       = v[4:9]
        res       = v[9:]
        cellphone = f'+{cod} ({ddd}) {pre}-{res}'
    if database == 'varejao': 
        name      = contact['name']
        cellphone = contact['cellphone']   
    return name,cellphone


# Test cellphone input
def test_phone(phone):
    if type(phone) == str:
        if len(phone) == 13: 
            if phone.isdigit(): return phone
            else:               return None
        else: return None
    else: return None    
            
# Test name input            
def test_name(name,market,config):
    if type(name) == str:
        if len(name.strip()) <= config[market]['sizename']: return name
        else:                                               return None
    else: return None

# Create engine
def c_engine(market,config):
    db_user = config[market]['user']
    db_pwd  = config[market]['password']
    db_host = config[market]['host']
    db_port = config[market]['port']
    db_name = config[market]['database']    
    if market == 'macapa':  engine = db.create_engine(f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}')
    if market == 'varejao': engine = db.create_engine(f'postgresql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}')
    return engine

# Insert contacts on database
def insert(connection,market,n,c):
    connection.execute(f"INSERT INTO contacts (nome,celular) VALUES ('{n}','{c}');")
