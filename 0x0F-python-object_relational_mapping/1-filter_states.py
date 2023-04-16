#!/usr/bin/python3

import MySQLdb
import sys

"""Get username, password and database name from command line arguments"""
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    """Connect to MySQL server running on localhost at port 3306"""

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        password=password,
        db=database
    )

    """ Create a cursor 0bject"""
    cursor = db.cursor()

    """Build the SQL Query"""
    query = """SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"""

    """execute the query"""
    cursor.execute(query)

    """Fetch all the rows"""
    rows = cursor.fetchall()

    """Print the results"""
    for row in rows:
        print(row)

    """ Close the cursor and database connections"""
    db.close()
