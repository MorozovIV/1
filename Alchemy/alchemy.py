from sqlalchemy import create_engine, Column, Integer, String
engine = create_engine('sqlite:///webinar.db', echo=True)
# engine = create_engine('sqlite:///c:\\SQLite\\Base\\webinar.db', echo=True)
from sqlalchemy.ext.declarative import declarative_base
base = declarative_base()
class User(base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    def __repr__(self):
        return '<User(name="{}", fullname="{}")>'.format(self.name, self.fullname)
User
dir(User)

    base.metadata.create all()