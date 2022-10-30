from mongoengine import Document, IntField, ListField, StringField

class ListModel(Document):
    id_user = IntField() # User id from User table
    list_name = StringField()
    data = ListField() # List of strings