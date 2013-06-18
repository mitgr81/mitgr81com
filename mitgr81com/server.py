import importlib
from flask import Flask

app = Flask(__name__)
app.config.from_object('config')


def tryregister(app, module, prefix=''):
    try:
        bar = importlib.import_module('{}.views'.format(module))
        app.register_blueprint(getattr(bar, 'views'), url_prefix=prefix)
        print('Registered "{}".'.format(module))
    except Exception as e:
        print('Module "{}" not found, did not register it: {}'.format(module, e))

tryregister(app, 'app2')
tryregister(app, 'unclear', prefix='/unclear')
tryregister(app, 'pants')


@app.route('/')
def index():
    return "hello"


@app.template_filter('plural')
def plural(counter):
    return 's' if counter > 1 else ''

#need some models http://pythonhosted.org/Flask-SQLAlchemy/index.html
#http://lucumr.pocoo.org/2011/7/19/sqlachemy-and-you/
