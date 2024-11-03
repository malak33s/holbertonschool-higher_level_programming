#!/usr/bin/python3
"""
Affiche toutes les villes d'un état donné, triées par `cities.id`.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=user, passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute(
        "SELECT cities.id, cities.name, states.name "
        "FROM cities JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )
    cities = cursor.fetchall()

    for city in cities:
        print(city)

    cursor.close()
    db.close()
