# import os
# _basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

ADMINS = frozenset(['youremail@yourdomain.com'])
SECRET_KEY = 'ty6dccqh^-9+yfunak!r6(g1ehbm7=wpds!9a!8kj((g=62@_y'

# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost/mitgr81com_dev'
SQLALCHEMY_BINDS = {
    'drupalchemy':        'mysqldb://root@localhost/cmcgraw_lodgenetcomwhatever',
}

DATABASE_CONNECT_OPTIONS = {}
