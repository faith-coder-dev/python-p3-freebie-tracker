#!/usr/bin/env python3
"""
test.py - Test all the methods and relationships

"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie

if __name__ == '__main__':
    # Connect to database
    engine = create_engine('sqlite:///freebies.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    
    print("\n" + "="*60)
    print("FREEBIE TRACKER - TEST & DEMO")
    print("="*60)
    
    # Get all freebies and show details
    print("\n ALL FREEBIES IN THE SYSTEM:")
    print("-" * 60)
    for freebie in session.query(Freebie).all():
        print(f"   {freebie.print_details()}")
    
    # Get one developer and show their freebies
    print("\n  JOHN'S FREEBIES:")
    print("-" * 60)
    john = session.query(Dev).filter_by(name='John').first()
    for freebie in john.freebies:
        print(f"   - {freebie.item_name} (Value: {freebie.value})")
    
    # Show which companies John got freebies from
    print("\n COMPANIES JOHN GOT FREEBIES FROM:")
    print("-" * 60)
    for company in john.companies:
        print(f"   - {company.name}")
    
    # Check if John received a T-Shirt
    print("\n DID JOHN RECEIVE A T-SHIRT?")
    print("-" * 60)
    has_shirt = john.received_one('T-Shirt')
    print(f"   Answer: {has_shirt}")
    
    #  Check if John received a Laptop
    print("\n  DID JOHN RECEIVE A LAPTOP?")
    print("-" * 60)
    has_laptop = john.received_one('Laptop')
    print(f"   Answer: {has_laptop}")
    
    #  Show all freebies from Safaricom
    print("\n  FREEBIES FROM SAFARICOM:")
    print("-" * 60)
    safaricom = session.query(Company).filter_by(name='Safaricom').first()
    for freebie in safaricom.freebies:
        print(f"   {freebie.print_details()}")
    
    #  Show all developers who got freebies from Safaricom
    print("\n  DEVELOPERS WHO GOT FREEBIES FROM SAFARICOM:")
    print("-" * 60)
    for dev in safaricom.devs:
        print(f"   - {dev.name}")
    
    #  Finds oldest company
    print("\n  OLDEST COMPANY:")
    print("-" * 60)
    oldest = session.query(Company).order_by(Company.founding_year).first()
    print(f"   {oldest.name} (Founded {oldest.founding_year})")
    
    #  Give a new freebie
    print("\n  GIVE JOHN A NEW FREEBIE (Laptop):")
    print("-" * 60)
    equity = session.query(Company).filter_by(name='Equity Bank').first()
    new_freebie = equity.give_freebie(john, 'Laptop', 50000)
    session.add(new_freebie)
    session.commit()
    print(f"   ✓ {new_freebie.print_details()}")
    
    #  Transfer a freebie between developers
    print("\n TRANSFER PEN FROM JOHN TO MARY:")
    print("-" * 60)
    pen = session.query(Freebie).filter_by(item_name='Pen').first()
    mary = session.query(Dev).filter_by(name='Mary').first()
    print(f"   Before: {pen.print_details()}")
    john.give_away(mary, pen)
    session.commit()
    print(f"   After:  {pen.print_details()}")
    
    print("\n" + "="*60)
    print(" TEST COMPLETE!")
    print("="*60 + "\n")
