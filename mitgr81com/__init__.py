import importlib
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

# from .unclear.views import unclear_views
# app.register_blueprint(unclear_views, url_prefix='/unclear')


def tryregister(app, module):
    try:
        bar = importlib.import_module('.views', '{}.{}'.format(app.import_name, module))
        app.register_blueprint(getattr(bar, 'unclear_views'), url_prefix='/{}'.format(module))
        print('Registered {}.'.format(module))
    except:
        print('Module "{}" not found, did not register it.'.format(module))

tryregister(app, 'unclear')
tryregister(app, 'pants')


@app.route('/')
def index():
    return "hello"


@app.template_filter('plural')
def plural(counter):
    return 's' if counter > 1 else ''

#need some models http://pythonhosted.org/Flask-SQLAlchemy/index.html
#http://lucumr.pocoo.org/2011/7/19/sqlachemy-and-you/
