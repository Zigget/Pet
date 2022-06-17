'''
All code was assembled by myself, Samuel Sidzyik.
I pulled bits and pieces from various sources but not one line of this file was written by anyone other than myself.

'''
import psycopg2
import dotenv
import os

#Check pet insurability and cost
#
#
#
#
#

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
