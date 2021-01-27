from sqlalchemy import create_engine
# Nos permite tener acceso a las funcionalidades de ORM de sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///newspaper.db')

Session = sessionmaker(bind=engine)

# Esta es la clase base de la cuál van a extender todos nuetros modelos
Base = declarative_base()