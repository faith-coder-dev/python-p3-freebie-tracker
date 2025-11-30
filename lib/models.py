from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


convention = {"fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s"}
metadata = MetaData(naming_convention=convention)
Base = declarative_base(metadata=metadata)



class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())

    freebies = relationship('Freebie', backref='company')
    
    devs = relationship('Dev', secondary='freebies', backref='companies', viewonly=True)

    def __repr__(self):
        return f'<Company {self.name}>'

    def give_freebie(self, dev, item_name, value):
        """Create a new freebie from this company to a dev."""
        freebie = Freebie(dev=dev, company=self, item_name=item_name, value=value)
        return freebie

    @classmethod
    def oldest_company(cls):
        """Find company with earliest founding year."""
        pass



class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    
    freebies = relationship('Freebie', backref='dev')

    def __repr__(self):
        return f'<Dev {self.name}>'

    def received_one(self, item_name):
        """Check if dev has received this item."""
        return any(freebie.item_name == item_name for freebie in self.freebies)

    def give_away(self, dev, freebie):
        """Transfer a freebie to another dev."""
        if freebie in self.freebies:
            freebie.dev = dev



class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer(), primary_key=True)
    dev_id = Column(Integer(), ForeignKey('devs.id'), nullable=False)
    company_id = Column(Integer(), ForeignKey('companies.id'), nullable=False)
    item_name = Column(String())
    value = Column(Integer())

    def __repr__(self):
        return f'<Freebie {self.item_name}>'

    def print_details(self):
        """Show who got what from which company."""
        return f'{self.dev.name} owns a {self.item_name} from {self.company.name}'
