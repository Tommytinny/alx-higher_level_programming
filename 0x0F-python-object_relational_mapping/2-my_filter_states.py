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
    query = f"SELECT * FROM states WHERE name = '{matchName}'"
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()
