from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, _id, name, email) -> None:
        self.id = _id
        self._name = name
        self._email = email
    
    @staticmethod
    def get(userid, _db):
        cursor = _db.get_db()
        cursor.execute("SELECT * FROM userdata where id='{}'".format(userid))
        result = cursor.fetchone()
        if not result:
            return None
        return User(result[0], result[1], result[2])        
    

    @staticmethod
    def create(userid, name, email, _db):
        cursor = _db.get_db()
        cursor.execute("INSERT INTO userdata values('{0}', '{1}', '{2}')".format(userid, name, email))
        cursor.execute("commit")

        return User(userid, name, email)        
    