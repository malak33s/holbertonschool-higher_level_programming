#!/usr/bin/python3
"""
List all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


def list_cities_by_states():
    """Connect to MySQL and list all cities with their corresponding states"""
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    list_cities_by_states()
