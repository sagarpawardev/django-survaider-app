'''
Created on 30-Apr-2017

@author: sagar
'''
from pymongo.mongo_client import MongoClient
from app.exception.NoSuchStateException import NoSuchStateException
from app.config.Credentials import URI, USERNAME, PASSWORD
from app.config.Collections import MAHARASHTRA, ADMIN


class DBConnection:
    def __init__(self, state):
        self.state = state
    
    def get(self):
        client = MongoClient(URI)
        client.edutracenextgen.authenticate(USERNAME, PASSWORD, source=ADMIN)
        if(self.state == MAHARASHTRA):
            return client.edutracenextgen.maharashtra
        
        raise NoSuchStateException(self.state)    