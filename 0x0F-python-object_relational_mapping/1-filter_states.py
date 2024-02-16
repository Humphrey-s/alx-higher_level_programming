#!/usr/bin/python3
#script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa
import MySQLdb
import sys

def main():

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    try:
        dbase =MySQLdb.connect(host="localhost", port=3306, user=username, password=password, database=db_name, charset="utf8")
    except Exception:
        print("connection failed")

    cursor = dbase.cursor()

    cursor.execute("SELECT * FROM {}.states WHERE states.id > 3 ORDER BY states.id ASC;".format(db_name))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    dbase.close()

if __name__ == "__main__":
    main()
