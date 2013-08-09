import importlib
from flask import Flask, redirect, url_for

app = Flask(__name__)
app.config.from_object('config')


def tryregister(app, module, prefix=''):
    try:
        bar = importlib.import_module('{}.views'.format(module))
        app.register_blueprint(getattr(bar, 'views'), url_prefix=prefix)
        print('Registered "{}".'.format(module))
    except Exception as e:
        print('Module "{}" not found, did not register it: {}'.format(module, e))

tryregister(app, 'unclear', prefix='/unclear')


@app.route('/')
def index():
    return redirect(url_for('unclear_views.views'))  #for now, but lets get the blog going here!


@app.template_filter('plural')
def plural(counter):
    return 's' if counter > 1 else ''

#need some models http://pythonhosted.org/Flask-SQLAlchemy/index.html
#http://lucumr.pocoo.org/2011/7/19/sqlachemy-and-you/
