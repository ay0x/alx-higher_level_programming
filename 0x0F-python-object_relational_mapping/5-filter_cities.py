#!/usr/bin/python3
"""
Lists all cities from a state in the database
"""
import sys
import MySQLdb

if __name__ == '__main__':
    count = 0
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306, charset="utf8")

    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
    FROM cities
    LEFT JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC""")
    cities = cur.fetchall()

    for city in cities:
        if city[2] == sys.argv[4]:
            if count > 0:
                print(", ", end="")
            print(city[1], end="")
            cont = cont + 1
    print()
    cur.close()
    db.close()
