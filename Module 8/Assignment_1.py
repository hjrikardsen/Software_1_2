import mysql.connector

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    database = "flight_game",
    user = "root",
    password = "password",
    autocommit = True
)

def get_airport_information(id):
    sql = f"SELECT name, municipality FROM airport WHERE ident = '{id}'"

    cursor = connection.cursor()
    cursor.execute(sql)

    data = cursor.fetchall()
    return data

ident_code = input("Enter the ICAO code of an aiport: ")

data = get_airport_information(ident_code)

print(f"Airport name: {data[0][0]}\nLocation: {data[0][1]}")