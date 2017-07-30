from mongoengine import signals
from flask import url_for
import os

from application import db
from utilities.common import utc_timestamp as now
from settings import STATIC_IMAGE_URL, AWS_BUCKET, AWS_CONTENT_URL


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
    bio=db.StringField(db_field='b', max_length=160)
    email_confirmed=db.BooleanField(db_field="ecf", default=False)
    change_configuration=db.DictField(db_field="cc")  #stores json dictionary which contails old email to new email
    profile_image = db.StringField(db_field="i", default=None)
    
    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.username = document.username.lower()
        document.email = document.email.lower()
    
    def profile_imgsrc(self, size):
        ''' this method fetches user's image url'''
        if AWS_BUCKET:
            #returning full path; gives full http
            return os.path.join(AWS_CONTENT_URL, AWS_BUCKET, 'user', '%s.%s.%s.png' % (self.id, self.profile_image, size))
        else:
           
            return url_for('static', filename=os.path.join(STATIC_IMAGE_URL, 'user', '%s.%s.%s.png' % (self.id, self.profile_image, size)))
            
    meta={
        'indexes': ['username', 'email', '-created']
    }    
    
signals.pre_save.connect(User.pre_save, sender=User)
    
    
    
    
    