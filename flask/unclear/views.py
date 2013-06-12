from flask import Blueprint, render_template, request
from flask.views import MethodView

unclear_views = Blueprint('unclear_views', __name__, template_folder='templates')


class PassphraseView(MethodView):

    def get(self, passphrase_id=None):
        if passphrase_id is None:
            return render_template('form.html')
        else:
            return render_template('unlock.html', object={})

    def post(self):
        print("Passphrase is " + request.values['passphrase'])
        print("Unlock phrase is " + request.values['unlock_phrase'])
        print("Max Access is " + request.values['max_access'])
        return render_template('thanks.html', full_uri="eeaosu", passphrase={'id': 'aabbcc112233'})

    def patch(self, passphrase_id):
        return "kk"


unclear_views.add_url_rule('/', view_func=PassphraseView.as_view('unclear_views'))
unclear_views.add_url_rule('/<passphrase_id>', view_func=PassphraseView.as_view('unclear_views'))
#Using pluggable views http://flask.pocoo.org/docs/views/
# and blueprints http://flask.pocoo.org/docs/blueprints/
