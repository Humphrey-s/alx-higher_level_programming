#!/usr/bin/python3
"""
 a python file that contains the class definition of a State and an instance Base = declarative_base()
"""
import sys
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
import MySQLdb as _mysql


Base = declarative_base()

class State(Base):
    """
    State table class
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(288), nullable=False)
