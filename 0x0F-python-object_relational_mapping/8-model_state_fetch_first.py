#!/usr/bin/python3
"""module lists first state object from database hbtn_0e_6_usa using SQLAlchemy
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import inspect

if __name__ == "__main__":
    username = argv[1]
    passwd = argv[2]
    db = argv[3]

    # setup engine
    engine_string = "mysql://{}:{}@localhost:3306/{}".format(username,
                                                             passwd, db)
    # default username: root, passwd: "", db: hbtn_0e_6_usa
    engine = create_engine(engine_string)
    Base.metadata.bind = engine

    # setup session
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    """
    # check table
    inspector = inspect(engine)
    table_list = inspector.get_table_names()
    if 'states' not in table_list:
        print("not in list")
    else:
        print("in list")
    """

    first = session.query(State).first()
    if first is None:
        print("Nothing")
    else:
        print("{}: {}".format(first.id, first.name))
