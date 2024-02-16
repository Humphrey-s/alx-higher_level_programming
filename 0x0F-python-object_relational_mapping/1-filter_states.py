#!/usr/bin/python3
import MySQLdb
import sys

def main():

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    dbase =MySQLdb.connect(host="localhost", port=3306, user=username, password=password, database=db_name, charset="utf8")

    cursor = dbase.cursor()

    cursor.execute("SELECT states.id, states.name FROM {}.states WHERE states.id > 3 ORDER BY states.id ASC".format(db_name))
    
    rows = cursor.fetchall()

    for row in rows:
        print(row)

if __name__ == "__main__":
    main()
