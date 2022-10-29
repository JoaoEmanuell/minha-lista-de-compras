from mongoengine import Document, IntField, ListField

class ListModel(Document):
    id_user = IntField() # User id from User table
    data = ListField() # List of strings