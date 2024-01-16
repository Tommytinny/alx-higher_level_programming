#!/usr/bin/python3
""" Relationship State and cities """
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

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state_to_create = State(name="California")
    session.add(state_to_create)
    session.commit()
    city_to_create = City(name="San Francisco", state_id=state_to_create.id)
    session.add(city_to_create)
    session.commit()

    session.close()
