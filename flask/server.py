#!/usr/bin/env python
from flask import Flask
from unclear.views import unclear_views

app = Flask(__name__)
app.register_blueprint(unclear_views, url_prefix='/unclear')


@app.route('/')
def index():
    return "hello"


@app.template_filter('plural')
def plural(counter):
    return 's' if counter > 1 else ''

if __name__ == '__main__':
    app.run(debug=True)


#need some models http://pythonhosted.org/Flask-SQLAlchemy/index.html
#http://lucumr.pocoo.org/2011/7/19/sqlachemy-and-you/
