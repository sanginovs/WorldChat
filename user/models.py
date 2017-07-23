from application import db
from utilities.common import utc_timestamp as now


class User(db.Document):
    #db_field is the name of the field in the actual document 
    #db_field converts all the username field to u which saves a lot of memory
    #in the database
    username= db.StringField(db_field="u", required=True, unique=True)
    password = db.StringField(db_field="p", required=True)
    email=db.EmailField(db_field="e", required=True, unique=True)
    first_name=db.StringField(db_field="fn", max_length=50)
    last_name=db.StringField(db_field="ln", max_length=50)
    created=db.IntField(db_field="c", default=now()) #don't store dates but store timestamp in UTC
    bio=db.StringField(db_field='b', max_length=50)
    
    
    meta={
        'indexes': ['username', 'email', '-created']
    }    
    
    