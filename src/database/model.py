'''
Created on 22.04.2017

@author: pro
'''

from sqlalchemy import MetaData, Table, Column, Integer, String, \
    ForeignKey, create_engine,LargeBinary
from sqlalchemy.orm import mapper, relationship, sessionmaker
from sqlalchemy.pool import StaticPool

class User(object):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    def __repr__(self):
        return "User: %s with ID: %i" % (self.name, self.user_id )
class Message(object):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    def __repr__(self):
        return "Message from %s to %s" % (self.origin, self.destination)

def create_database(url):
    metadata = MetaData()

    user_table = Table('user', metadata,
       Column('user_id', Integer, primary_key=True),
       Column('name', String(50)),
       Column('public_key',LargeBinary())
    )
    
    
    message_table = Table('message', metadata,
        Column('message_id', Integer, primary_key=True),
        Column('origin', Integer),
        Column('destination', Integer, ForeignKey('user.user_id')),
        Column('type',Integer),
        Column('timestamp',Integer),
        Column('publickey',LargeBinary()),
        Column('content', LargeBinary()),
        Column('key', LargeBinary()),
        Column('iv', LargeBinary()),
        Column('signature', LargeBinary())
    )

    message_mapper = mapper(Message, message_table,
                           polymorphic_identity='message')
    mapper(User, user_table, properties={
        'messages': relationship(Message, lazy=True, backref='user')
    })
    engine = create_engine('sqlite:///'+url, echo=False,connect_args={'check_same_thread':False},
                    poolclass=StaticPool)
    metadata.create_all(engine)
    return engine
def create_session(engine):
    return sessionmaker(engine)()
def test(session):
    user1 = User(name='User1')
    user1.messages.append(Message())
    session.add(user1)
    session.commit()
    c = session.query(User).get(1)
    print c
if __name__ == '__main__':
    engine = create_database("")
    session =  create_session(engine)
    test(session)
