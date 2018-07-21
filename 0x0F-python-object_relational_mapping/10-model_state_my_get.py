#!/usr/bin/python3
"""module prints state object argument from database using SQLAlchemy
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":

    username = argv[1]
    passwd = argv[2]
    db = argv[3]
    state_obj = argv[4]

    # setup engine
    engine_string = "mysql://{}:{}@localhost:3306/{}".format(username,
                                                             passwd, db)
    # default username: root, passwd: "", db: hbtn_0e_6_usa
    engine = create_engine(engine_string)
    Base.metadata.bind = engine

    # setup session
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    list = session.query(State).order_by(State.id).all()
    found_flag = 0
    for obj in list:
        if obj.name == state_obj:
            print("{}".format(obj.id))
            found_flag = 1
    if found_flag == 0:
        print("Not found")
