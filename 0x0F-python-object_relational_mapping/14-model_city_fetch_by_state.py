#!/usr/bin/python3
"""module lists all city objects from database using SQLAlchemy
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

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

    state_list = session.query(State).order_by(State.id).all()
    city_list = session.query(City).order_by(City.id).all()

    for elem in city_list:
        # inner loop retrieves state name
        for obj in state_list:
            if obj.id == elem.state_id:
                state_name = obj.name
        print("{}: ({}) {}".format(state_name, elem.id, elem.name))
