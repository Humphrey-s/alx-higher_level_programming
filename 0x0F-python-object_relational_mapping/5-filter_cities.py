#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb as _mysql
import sys

def main():

    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = _mysql.connect(host="localhost", user=user, passwd=passwd, db=db_name)

    cursor = db.cursor()

    cursor.execute("SELECT cities.name FROM {}.cities JOIN {}.states WHERE cities.state_id = (SELECT states.id FROM {}.states WHERE states.name = BINARY '{:s}') GROUP BY cities.id ORDER BY cities.id".format(db_name, db_name, db_name, state_name))

    rows = cursor.fetchall()

    for i in range(0, len(rows)):

        print(rows[i][0], end="")
        try:
            if rows[i + 1] is not None:
                print(", ", end="")
        except Exception:
            print("")

if __name__ == "__main__":
    main()
