#!/usr/bin/python3
"""
Filter states that start with 'N' from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


def filter_states():
    """Connect to MySQL and list states starting with 'N'"""
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    filter_states()
