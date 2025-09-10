import mysql.connector

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    database = "flight_game",
    user = "root",
    password = "password",
    autocommit = True
)

def get_airports_by_country(country_code):
    sql = f"SELECT type FROM airport WHERE iso_country = '{country_code}'"

    cursor = connection.cursor()
    cursor.execute(sql)

    data = cursor.fetchall()
    return data





def run_country_program(country_code1):

    airport_types = get_airports_by_country(country_code1)

    counter_small = 0
    counter_medium = 0
    counter_heliport = 0
    counter_large = 0



    for i in airport_types:
        if i[0] == "small_airport":
            counter_small += 1
        elif i[0] == "medium_airport":
            counter_medium += 1
        elif i[0] == "large_airport":
            counter_large += 1
        elif i[0] == "heliport":
            counter_heliport += 1

    return (counter_small, counter_medium, counter_heliport, counter_large)



country_code = input("Enter the country code (e.g., FI for Finland): ")

data_tuple = run_country_program(country_code)

print(f"Airports in {country_code}:")
print(f"{data_tuple[0]} small_airport airports\n{data_tuple[1]} medium_airport airports\n{data_tuple[2]} heliport airports\n{data_tuple[3]} large_airport airports")
