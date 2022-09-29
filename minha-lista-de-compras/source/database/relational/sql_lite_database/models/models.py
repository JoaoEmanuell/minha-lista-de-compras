from orm_sqlite import Model, StringField, IntegerField

class UserModel(Model):
    id = IntegerField(primary_key=True)
    username = StringField()
    password = StringField()
