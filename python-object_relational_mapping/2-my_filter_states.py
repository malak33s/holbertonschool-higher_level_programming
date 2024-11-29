#!/usr/bin/python3
"""
Filter states by user input from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


def filter_states_by_input():
    """Connect to MySQL and filter states by user input"""
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(sys.argv[4])
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    filter_states_by_input()
