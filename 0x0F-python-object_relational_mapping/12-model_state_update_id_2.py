#!/usr/bin/python3
""" Update id 2 """

import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2],
                sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = "New Mexico"

    state_to_update = session.query(State).\
        filter(State.id == 2).first()

    if state_to_update:
        state_to_update.name = new_state
        session.commit()

    session.close()
