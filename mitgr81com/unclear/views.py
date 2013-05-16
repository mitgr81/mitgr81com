from django.views.generic import CreateView, DetailView

from .models import PassphraseHash


class UnclearCreate(CreateView):
    model = PassphraseHash


class UnclearDetail(DetailView):
    model = PassphraseHash


class UnclearThanks(UnclearDetail):
    template_name = 'unclear/passphrasehash_thanks.html'
