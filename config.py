WTF_CSRF_ENABLED = True  # activate cross-site request forgery
SECRET_KEY = 'you-will-never-guess'  # cryptographic token when above line is enabled

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

