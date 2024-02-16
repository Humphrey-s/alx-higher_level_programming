#!/usr/bin/python3
#script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa

if __name__ == "__main__":
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    try:
        dbase =MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name, charset="utf8")
    except Exception:
        print("connection failed")
        exit(0)

    cursor = dbase.cursor()

    cursor.execute("SELECT * FROM {}.states WHERE states.name LIKE BINARY 'N%' ORDER BY states.id ASC;".format(db_name))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    dbase.close()
