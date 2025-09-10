import mysql.connector
from geopy.distance import geodesic, great_circle

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    database = "flight_game",
    user = "root",
    password = "password",
    autocommit = True
)


def get_airport_coordinates(icao_code):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{icao_code}'"

    cursor = connection.cursor()
    cursor.execute(sql)

    data = cursor.fetchall()
    return data



def run_airport_distance():
    icao_code1 = input("Enter the ICAO code of the first airport: ")
    icao_code2 = input("Enter the ICAO code of the second airport: ")

    coordinates1 = get_airport_coordinates(icao_code1)
    coordinates2 = get_airport_coordinates(icao_code2)

    print(f"Distance between {icao_code1} and {icao_code2}: {geodesic(coordinates1[0], coordinates2[0]).km:.2f} kilometers (by geodesic).")
    print(f"Distance between {icao_code1} and {icao_code2}: {great_circle(coordinates1[0], coordinates2[0]).km:.2f} kilometers (by great_circle).")

run_airport_distance()


