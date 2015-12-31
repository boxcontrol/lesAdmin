from app import app, db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), index=True, unique=True)
    password = db.Column(db.String(255), index=True, unique=True)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id) # python 2
        except NameError:
            return str(self.id) # python 3

    def __repr__(self):
        return '<User %r>' % self.username



class Server(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    server_name = db.Column(db.String(), index=True, unique=True)
    server_API_key = db.Column(db.String(), index=False, unique=False)
    server_API_hash = db.Column(db.String(), index=False, unique=True)
    server_location = db.Column(db.String(), index=True, unique=False)
    server_API_url = db.Column(db.String(), index=True, unique=False)
    server_description = db.Column(db.String(), index=True, unique=False)

    def __init__(self, server_name, server_API_key,
                 server_API_hash, server_API_url,
                 server_location='', server_description=''):
        self.server_name = server_name
        self.server_API_key = server_API_key
        self.server_API_hash = server_API_hash
        self.server_API_url = server_API_url
        self.server_location = server_location
        self.server_description = server_description

    def __repr__(self):
        return '<server %r>' % self.server_name


