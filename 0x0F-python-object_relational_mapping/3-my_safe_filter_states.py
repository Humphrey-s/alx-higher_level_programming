#!/usr/bin/python3
"""
a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time, write one that is safe from MySQL injections
"""
import MySQLdb as _mysql
import sys

def main():

    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    array = state_name.split("\'")
    state_name = array[0]

    db = _mysql.connect(host="localhost", port=3306, user=user, passwd=passwd, db=db_name)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM {}.states WHERE name = BINARY '{:s}' ORDER BY states.id ASC".format(db_name, state_name))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

if __name__ == "__main__":
    main()
