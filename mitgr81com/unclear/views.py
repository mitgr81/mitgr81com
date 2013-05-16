import string
import random
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, DetailView, TemplateView

from .models import PassphraseHash


class UnclearCreate(CreateView):
    model = PassphraseHash

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.slug = u''.join([random.choice(string.ascii_letters + string.digits + '-_') for ch in range(8)])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class UnclearDetail(DetailView):
    model = PassphraseHash


class UnclearThanks(DetailView):
    template_name = 'unclear/passphrasehash_thanks.html'
    model = PassphraseHash
