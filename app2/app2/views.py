from flask import Blueprint, request
from flask.views import MethodView

from .models import TestModel

views = Blueprint('app2views', __name__, template_folder='templates', static_folder='static')


class NuggetView(MethodView):

    def get(self, passphrase_id=None):
        if passphrase_id is None:
            passphrase = TestModel('test')
            passphrase.save()
            return "no ID(ea)"
        else:
            thingy = TestModel.query.get_or_404(passphrase_id)
            return unicode(thingy)

view_obj = NuggetView.as_view('views')
views.add_url_rule('/images', view_func=view_obj)
views.add_url_rule('/images/<passphrase_id>', view_func=view_obj)
#Using pluggable views http://flask.pocoo.org/docs/views/
# and blueprints http://flask.pocoo.org/docs/blueprints/
