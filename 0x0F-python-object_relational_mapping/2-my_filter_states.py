#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the states table 
of hbtn_0e_0_usa where name matches the arguments
"""
import sys
import MySQLdb as _mysql

def main():

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    dbase =_mysql.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)

    cursor = dbase.cursor()

    cursor.execute("SELECT * FROM {}.states WHERE states.name = BINARY '{:s}'".format(db_name, state_name))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    dbase.close()

if __name__ == "__main__":
    main()
