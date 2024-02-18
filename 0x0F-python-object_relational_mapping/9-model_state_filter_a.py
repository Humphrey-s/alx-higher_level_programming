#!/usr/bin/python3
"""
a script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import select, create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def main():

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(sys.argv[1], sys.argv[2], sys.argv[3]))

    with Session(engine) as session, session.begin():

        states = session.query(State).where(State.name.like('%a%')).group_by(State.id).order_by(State.id).all()

        for obj in states:
            print("{}: {}".format(obj.id, obj.name))


if __name__ == "__main__":
    main()
