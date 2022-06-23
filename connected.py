'''
All code was assembled by myself, Samuel Sidzyik.
I pulled bits and pieces from various sources but not one line of this file was written by anyone other than myself.

'''
#Display 'start/current? date' of program

#1-Check pet insurability and cost *1
#2-Policyowner options
#   -Add pet to policy *1
#   -Remove pet from policy
#   -File Claim
#   -Print policy
#3-Agent options (token login)
#   -Policy cost chart over time (Numpy per pet and combined)
#   -Agent's policyowners (pandas 2D)(3D over time?)
#4-Actuary options (G-Auth)
#   -Access Agent cut
#       -Current commission percentage
#       -Individual agents commission
#       -Total Amount of all agents paid next month
#   -Access death values
#       -Print Values (csv/json)
#       -Change Values (sql)
#       -Project Values (seaborn?)
#5-Time Travel*
#   *Moves start date forward
#   *Collects premium
#   *Auto kills pets(gently, lol)
#6-Quit

import getpass
import datetime
import psycopg2
import dotenv
import os


'''
Values for testing
'''
breedsdict = {  'Lab':{'size':'L','lifespan':11},
                'Shepherd':{'size':'M','lifespan':9},
                'Yippie':{'size':'XS','lifespan':15},
                'Monster':{'size':'XL','lifespan':7}}

claimdict = {   'XS':110,
                'S':125,
                'M':140,
                'L':180,
                'XL':210
}


'''
Functions
'''
def insurability():
    dog = input('What is the breed of your pal?\nIf mixed or unkown type 0: ')
    if dog in breedsdict:
        #elif breed in Dog API weight
        size = breedsdict[dog]['size'] #or API weight
        lifespan = breedsdict[dog]['lifespan']
    else:
        weight = int(input('\nEnter your doggo\'s weight or guesstimate adult weight if a puppy: '))
        if weight < 15:
            size = 'XS'
            lifespan = 18
        elif weight < 30:
            size = 'S'
            lifespan = 15
        elif weight < 65:
            size = 'M'
            lifespan = 12
        elif weight < 110:
            size = 'L'
            lifespan = 9
        else:
            size = 'XL'
            lifespan = 7
    age = int(input('\nHow many years young is your doggo?: '))
    lifeleft = lifespan - age
    quote = claimdict[size]/lifeleft
    return quote
def login():
    pass
def signup():
    pass

'''
Objects
'''
class Customer():
    def __init__(self):
        pass
    def addpet(self):
        quote = insurability()
        print(quote)
    def removepet(self):
        pass
    def fileclaim():
        pass
    def printpolicy():
        pass
class Agent():
    def __init__(self):
        pass
    def 
class Actuary():
    pass

'''
Program Navigation
'''
monthy = 'May'
yeary = '1999'
print('\nWelcome to Sam\'s Pet Insurance!!')
while True:
    match input('\nYou are in {} of {}\nWhere would you like to go?\n[1] Check you Pet!\n[2] Customer Portal\n[3] Agent Portal\n[4] Actuarial Portal\n[5] Time Travel\n[6] Goodbye\n'.format(monthy,yeary)):
        case '1':
            quote = insurability()
            if quote > 10:
                print('To insure you doggo the annual premium would be ${:,.2f}'.format(quote))
            else:
                print('It isn\'t worth it for us to insure your doggo')
            pass
        case '2':
            print('Made it to Customer Portal')
            while True:
                match input('\n[1] Login\n[2] Sign Up\n[3] Back\n'):
                    case '1':
                        pass
                    case '2':
                        pass
                    case '3':
                        break
                    case _:
                        print('This was an invalid selection')
                        pass
        case '3':
            print('Made it to Agent Portal')
            while True:
                match input('\n[1] Login\n[2] Back\n'):
                    case '1':
                        pass
                    case '2':
                        break
                    case _:
                        print('This was an invalid selection')
        case '4':
            print('Made it to Actuarial Portal')
            while True:
                match input('\n[1] Login\n[2] Back\n'):
                    case '1':
                        pass
                    case '2':
                        break
                    case _:
                        print('This was an invalid selection')
        case '5':
            print('Made it to the Time Machine')
            pass
        case '6':
            print('Thank you, Goodbye.')
            break
        case _:
            print('You did not enter a valid path')
            pass
'''
Establishes connection to Pet Database on Azure server
Framework for the connection pulled from Microsoft Azure's help file:
https://docs.microsoft.com/en-us/azure/postgresql/single-server/connect-python
'''
def test_connect():
    dotenv.load_dotenv(dotenv.find_dotenv())
    host = "pmisev1.postgres.database.azure.com"
    dbname = "PetFinal"
    user = "owner"
    password = os.getenv('password')
    sslmode = "require"
    # Construct connection string

    conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
    conn = psycopg2.connect(conn_string) 
    print("Connection established")
    cursor = conn.cursor()
    # Drop previous table of same name if one exists

    cursor.execute("DROP TABLE IF EXISTS inventory;")
    print("Finished dropping table (if existed)")
    # Create a table

    cursor.execute("CREATE TABLE inventory (id serial PRIMARY KEY, name VARCHAR(50), quantity INTEGER);")
    print("Finished creating table")
    # Insert some data into the table

    cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("banana", 150))
    cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("orange", 154))
    cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("apple", 100))
    print("Inserted 3 rows of data")
    # Clean up

    conn.commit()
    cursor.close()
    conn.close()
