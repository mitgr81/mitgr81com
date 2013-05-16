from django.views.generic import CreateView, DetailView

from .models import PassphraseHash


class UnclearCreate(CreateView):
    model = PassphraseHash


class UnclearDetail(DetailView):
    model = PassphraseHash


class UnclearThanks(DetailView):
    template_name = 'unclear/passphrasehash_thanks.html'
    model = PassphraseHash
