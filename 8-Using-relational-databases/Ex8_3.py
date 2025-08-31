from geopy import distance

from Ex8_1 import get_db_connection, execute_query, close_db_connection


def main():
    conn, cursor = get_db_connection()
    airports = []
    try:
        for name in ["first", "second"]:
            while True:
                icao = input(f"Please input the {name} ICAO: ")
                query = f"""SELECT latitude_deg, longitude_deg
        FROM airport WHERE ident = '{icao}'
        """
                rows = execute_query(cursor, query)
                if len(rows) == 0:
                    print(
                        f"There is no such airport with the icao {icao}. Please try again!"
                    )
                    continue
                airports.append(rows[0])
                break
        if len(airports) != 2:
            raise ValueError("Not correct number of airports recognized")
        dist = distance.distance(airports[0], airports[1])
        print(f"Distance between the two airports is: {dist}")
    finally:
        close_db_connection(conn, cursor)


if __name__ == "__main__":
    main()
