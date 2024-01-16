#!/usr/bin/python3
""" List states and cities """

import sys
from relationship_state import Base, State
from relationship_city import City

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2],
                sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(City, State)\
        .join(State, State.id == City.state_id)\
        .order_by(City.id)
    for city, state in result:
        print('{}: {} -> {}'.format(city.id, city.name, state.name))

    session.close()
