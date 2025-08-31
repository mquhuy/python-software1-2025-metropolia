from Ex8_1 import get_db_connection, execute_query, close_db_connection


def main():
    country_code = input("Please enter the area code: ")
    query = f"""SELECT airport.name, type, country.name FROM airport, country
WHERE airport.iso_country = '{country_code}'
AND airport.iso_country = country.iso_country
ORDER BY type"""
    conn, cursor = get_db_connection()
    try:
        rows = execute_query(cursor, query)
        if len(rows) == 0:
            print(f"There is no such country with code {country_code}")
            return
        country_airports = {}
        country_name = ""
        for row in rows:
            airport_name, airport_type, country_name = row
            airports_in_type = country_airports.get(airport_type, [])
            airports_in_type.append(airport_name)
            country_airports[airport_type] = airports_in_type
        print(f"{country_name} has:")
        for airport_type, airports_in_type in country_airports.items():
            print(
                f"- {len(airports_in_type)} {airport_type} airport(s): {", ".join(airports_in_type)}"
            )
    finally:
        close_db_connection(conn, cursor)


if __name__ == "__main__":
    main()
