#!/usr/bin/python3
"""A script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument"""

import MySQLdb
import sys

"""Get username, password and database name from command line arguments"""
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    """Connect to MySQL server running on localhost at port 3306"""

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        password=password,
        db=database,

    )

    """ Create a cursor to execute query"""
    cursor = db.cursor()

    """Prepare SQL querry to get all states where name matches argument"""
    sql = "SELECT * FROM states WHERE name = '{}' \
            ORDER BY id ASC".format(state_name)

    try:

        """execute the query"""
        cursor.execute(sql)

        """Fetch all the rows"""
        rows = cursor.fetchall()

        """Print the results"""
        for row in rows:
            print(row)

    except Exception as e:
        """print error messages"""
        print("Error: {}".format(e))

    """ Close the cursor and database connections"""
    db.close()
