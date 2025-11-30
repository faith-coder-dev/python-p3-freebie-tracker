#!/usr/bin/env python3
"""
debug.py - Tests code in Python console

Run: pipenv run python debug.py
Then you can type commands in the interactive shell to test things.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie

if __name__ == '__main__':
    # Connect to database
    engine = create_engine('sqlite:///freebies.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    
    print("\n✓ Database connected!")
    print("You can now test your code. Try:")
    print("   john = session.query(Dev).filter_by(name='John').first()")
    print("   print(john.freebies)")
    print("   print(john.companies)")
    print("\n")
    
    import ipdb; ipdb.set_trace()
