#!/usr/bin/python3
"""
a script that prints the first State object from the database hbtn_0e_6_usa
"""
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select
from model_state import Base, State
import sys


def main():

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(sys.argv[1], sys.argv[2], sys.argv[3]))

    with Session(engine) as session, session.begin():

        statement = select(State).where(State.id == 1)

        result = session.execute(statement)

        for obj in result.scalars():
            print("{}: {}".format(obj.id, obj.name))

if __name__ == "__main__":
    main()
