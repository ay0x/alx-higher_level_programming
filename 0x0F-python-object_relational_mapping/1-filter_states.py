#!/usr/bin/python3
"""
Lists all states with a name starting with N from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], database=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id;")
    states = cur.fetchall()

    for state in states:
        print(state)
