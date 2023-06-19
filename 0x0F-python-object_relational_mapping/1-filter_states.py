#!/usr/bin/python3
""" lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if _name_ == "_main_":
   db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], por06
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
