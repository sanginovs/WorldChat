
from mongoengine import CASCADE 
#cascade is a method so if the particular record is deleted, it deletes all the records that are
#related to it e.g if user profile is deleted, all his relationships get deleted too

from application import db
from utilities.common import utc_timestamp as now
from user.models import User

class Relationship(db.Document):
    
    
    FRIENDS = 1   #1 for friends; gets stored in a databases
    BLOCKED = -1  #-1 for blocked 
    
    
    #this is tuple so we have different choices; you cann either be friends or blocked
    #what gets saved in a database is 1 or -1 
    RELATIONSHIP_TYPE = (
        (FRIENDS, 'Friends'),
        (BLOCKED, 'Blocked'),
        )
        
    
    '''Friendship cycle:
    a) user A requests a friendship
    status=Pending
    b) User B approves
    status=Approved
    
    E.g
    Sher requests friendship to his girlfriend: Sher --> Fotima
    after it is requested, we will have relationship record for Sher:
    
    rel_record(type=Friends, status=Pending, to_user=Fotima)
    
    Now, Sher's girlfriend Fotima will get this request and new rel_record will be created for her too:
    
    rel_record(type=Friends, status=Pending, from_user=Sher); if she approves then status will be changed to Approved
    
    We could have just one rel_type for both of them. However, creating two allows for faster queries
    and allows scaling the application better.
    
    
    
    '''
    
    PENDING = 0
    APPROVED = 1
    
    STATUS_TYPE = (
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        )
        
    from_user = db.ReferenceField(User, db_field='fu', reverse_delete_rule=CASCADE) #foreign key to user table
    #reverse_delete_rule=Cascade: if user is deleted, all these relationship get deleted
    to_user = db.ReferenceField(User, db_field='tu', reverse_delete_rule=CASCADE)
    
    rel_type = db.IntField(db_field='rt', choices=RELATIONSHIP_TYPE)
    #rel_type choices queries from tuple
    status = db.IntField(db_field='s', choices=STATUS_TYPE)
    req_date = db.IntField(db_field='rd', default=now()) #date request was sent
    approved_date = db.IntField(db_field="ad", default=0) #date whether user B approves or not

    def is_friend(self, user):
        if user:
            return self.get_relationship(user, self.to_user)
        else:
            return None
    
    #this is a helper method to check relationship of users on a model level
    @staticmethod #allows to add static method to class
    def get_relationship(from_user, to_user):
        
        if from_user == to_user: #if you are looking at your own profile
            return 'SAME'
            
        #filter - Returns an array with only those elements that match the condition. The returned elements are in the original order.
        rel = Relationship.objects.filter(
            from_user=from_user,
            to_user=to_user
            ).first()
        if rel and rel.rel_type == Relationship.FRIENDS:
            if rel.status == Relationship.PENDING:
                return "FRIENDS_PENDING"
            if rel.status == Relationship.APPROVED:
                return "FRIENDS_APPROVED"
        elif rel and rel.rel_type == Relationship.BLOCKED:
            return "BLOCKED"
        else: #if the user has already requested a friend request from logged in user
            reverse_rel = Relationship.objects.filter(
                from_user=to_user,
                to_user=from_user
                ).first()
            if reverse_rel and reverse_rel.rel_type == Relationship.FRIENDS:
                if reverse_rel.status == Relationship.PENDING:
                    return "REVERSE_FRIENDS_PENDING"
            elif reverse_rel and reverse_rel.rel_type == Relationship.BLOCKED: #if user reverse blocked logged in user
                return "REVERSE_BLOCKED"
            return None

    
    meta = {
        'indexes': [('from_user', 'to_user'), ('from_user', 'to_user', 'rel_type', 'status')]
    }

'''    
    The $meta projection operator returns for each matching document 
    the metadata (e.g. "textScore") associated with the query.
    A $meta expression has the following syntax:
    { $meta: <metaDataKeyword> }
'''