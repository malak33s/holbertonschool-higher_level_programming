#!/usr/bin/python3
"""
Filter states by user input (safe from SQL injection)
"""
import MySQLdb
import sys


def safe_filter_states():
    """Connect to MySQL and filter states safely"""
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    safe_filter_states()
