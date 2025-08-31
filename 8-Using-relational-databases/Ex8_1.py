import mysql.connector

def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="huy",
        password="1234",
        database="flight_game",
    )

    cursor = conn.cursor()
    return conn, cursor

def execute_query(cursor, query):
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows

def close_db_connection(conn, cursor):
    cursor.close()
    conn.close()

def main():
    conn, cursor = get_db_connection()
    try:
        icao = input("Please input the ICAO:")
        query = f"""SELECT name, municipality
FROM airport WHERE ident = '{icao}'
"""
        rows = execute_query(cursor, query)
        if len(rows) == 0:
            print("There is no such airport in our database")
            return
        for row in rows:
            print(f"Airport name: {row[0]}, Town: {row[1]}")
    finally:
        close_db_connection(conn, cursor)

if __name__ == "__main__":
    main()
