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

        states = session.query(State).order_by(State.id).first()

        if states is None:
            print("Nothing")
        else:
            print("{}: {}".format(states.id, states.name))

if __name__ == "__main__":
    main()
