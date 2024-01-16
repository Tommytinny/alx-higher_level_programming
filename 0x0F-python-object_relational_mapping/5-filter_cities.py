#!/usr/bin/python3
""" List states """

if __name__ == "__main__":
    import MySQLdb
    import sys

    host = "localhost"
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    conn = MySQLdb.connect(
            host=host,
            user=username,
            passwd=password,
            db=database,
            port=3306
            )

    matchName = sys.argv[4]
    cursor = conn.cursor()
    query = """
    SELECT cities.id AS city_id,
    cities.name AS city_name,
    states.name AS state_name
    FROM states
    JOIN cities ON states.id = cities.state_id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (matchName,))
    rows = cursor.fetchall()

    city_name = ', '.join(row[1] for row in rows)
    print(city_name)

    cursor.close()
    conn.close()
