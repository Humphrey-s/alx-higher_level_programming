#!/usr/bin/python3
import sys
import MySQLdb as _mysql

def main():
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = _mysql.connect(charset="utf8", host="localhost", port=3306, user=username, password=password, database=db_name)
    c = db.cursor()
    c.execute("SELECT states.id, states.name FROM {}.states ORDER BY states.id ASC".format(db_name))
    rows = c.fetchall()

    for i in range(0, len(rows)):
        print(rows[i])

if __name__ == "__main__":
    main()
