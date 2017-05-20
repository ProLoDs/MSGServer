'''
Created on 22.04.2017

@author: pro
'''

from model import User,Message

def get_user_by_id(session,id):
    user = session.query(User).get(id)
    if user:
        return user
def get_user_by_name(session, name):
    user =  session.query(User).filter_by(name=name).one()
    if user:
        return user
def register_db(session,name,public_key):
    tmp_user = User(name=name,public_key = public_key)
    session.add(tmp_user)
    session.commit()
    return tmp_user.user_id

def add_message(session, message):
    tmp_user = session.query(User).get(message.origin)
    db_message = Message(origin=message.origin,
                         destination = message.destination,
                         key = message.key,
                         iv = message.iv,
                         content = message.message,
                         type = message.type,
                         timestamp = message.timestamp,
                         publickey = message.publickey,
                         signature = message.signature)
    tmp_user.messages.append(db_message)
    session.commit()
    pass
