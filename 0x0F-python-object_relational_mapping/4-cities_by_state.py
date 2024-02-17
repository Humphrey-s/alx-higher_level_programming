#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb as _mysql
import sys

def main():

    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    db = _mysql.connect(host="localhost", user=user, passwd=passwd, db=db_name)

    cursor = db.cursor()

    cursor.execute("SELECT cities.id, cities.name, states.name FROM {}.cities JOIN {}.states WHERE cities.state_id = states.id ORDER BY cities.id ASC".format(db_name, db_name))

    rows = cursor.fetchall()

    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
