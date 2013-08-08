from sqlalchemy import Column, Integer, String
from werkzeug.security import generate_password_hash, check_password_hash
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    gauth = Column(String(16), unique=True)
    email = Column(String(120), unique=True)
    password = Column(String(32), unique=True)

    def __init__(self, name=None, email=None, gauth=None, password=None):
        self.name = name
        self.email = email
        self.gauth = gauth
        self.password = generate_password_hash(password)

    def chk_passwd(self, password, provpassword=None):
        if not provpassword:
            return check_password_hash(self.pw_hash, password)
        else:
            return check_password_hash(provpassword, password)

    def __repr__(self):
        return '%r' % (str(self.name))

#class Paste(Base):
    #id = 