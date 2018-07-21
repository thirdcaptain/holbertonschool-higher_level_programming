#!/usr/bin/python3
"""module deletes all State objects with letter 'a' in db using SQLAlchemy
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import update

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

    list = session.query(State).order_by(State.id).all()
    for obj in list:
        for char in obj.name:
            if char == 'a':
                session.delete(obj)
                break
    session.commit()
