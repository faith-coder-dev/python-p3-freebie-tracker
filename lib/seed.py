#!/usr/bin/env python3
"""
seed.py - Creates sample data in the database

This file sets up the database with example companies, developers, and freebies.

"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

if __name__ == '__main__':
    # Connect to database
    engine = create_engine('sqlite:///freebies.db')
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Delete old data
    session.query(Freebie).delete()
    session.query(Dev).delete()
    session.query(Company).delete()
    session.commit()
    
    
    safaricom = Company(name='Safaricom', founding_year=1997)
    equity = Company(name='Equity Bank', founding_year=1984)
    iota = Company(name='IOTA', founding_year=2012)
    
    session.add_all([safaricom, equity, iota])
    session.commit()
    
    # Developers
    john = Dev(name='John')
    mary = Dev(name='Mary')
    peter = Dev(name='Peter')
    
    session.add_all([john, mary, peter])
    session.commit()
    
    # Create Freebies 
    free1 = Freebie(dev=john, company=safaricom, item_name='T-Shirt', value=500)
    free2 = Freebie(dev=john, company=equity, item_name='Pen', value=100)
    free3 = Freebie(dev=mary, company=safaricom, item_name='Cap', value=300)
    free4 = Freebie(dev=mary, company=iota, item_name='Notebook', value=200)
    free5 = Freebie(dev=peter, company=equity, item_name='USB Cable', value=400)
    
    session.add_all([free1, free2, free3, free4, free5])
    session.commit()
    
    print("\n✓ Database created successfully!\n")
