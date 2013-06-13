from flask import Blueprint, render_template, request, url_for
from flask.views import MethodView

from mitgr81com import db
from .models import PassphraseHash

unclear_views = Blueprint('unclear_views', __name__, template_folder='templates', static_folder='static')


class PassphraseView(MethodView):

    def get(self, passphrase_id=None):
        if passphrase_id is None:
            return render_template('form.html')
        else:
            return render_template('unlock.html', object=PassphraseHash.query.filter_by(slug=passphrase_id).limit(1).first_or_404())

    def post(self):
        passphrase = PassphraseHash(request.values['passphrase'], request.values['max_access'])
        passphrase.save()
        return render_template('thanks.html', passphrase=passphrase)

    def patch(self, passphrase_id):
        phrase = PassphraseHash.query.filter_by(slug=passphrase_id).limit(1).first_or_404()
        phrase.access_count += 1
        phrase.save()
        return "kk"
        # body = json.loads(request.body)
        # if 'decrypted' in body and body['decrypted']:
        #     this_hash = PassphraseHash.objects.get(slug=kwargs['slug'])
        #     this_hash.access_count += 1
        #     this_hash.save()

        #     return HttpResponse("okay!", content_type="application/json")
        # return HttpResponse("Nope", status=403)


unclear_views.add_url_rule('/', view_func=PassphraseView.as_view('unclear_views'))
unclear_views.add_url_rule('/<passphrase_id>', view_func=PassphraseView.as_view('unclear_views'))
#Using pluggable views http://flask.pocoo.org/docs/views/
# and blueprints http://flask.pocoo.org/docs/blueprints/
