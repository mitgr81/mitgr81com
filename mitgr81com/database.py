from flask.ext.sqlalchemy import SQLAlchemy

from .server import app
db = SQLAlchemy(app)

#need some models http://pythonhosted.org/Flask-SQLAlchemy/index.html
#http://lucumr.pocoo.org/2011/7/19/sqlachemy-and-you/
