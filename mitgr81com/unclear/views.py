from django.views.generic import CreateView, DetailView, ListView

from .models import PassphraseHash


class UnclearList(ListView):
    model = PassphraseHash


class UnclearCreate(CreateView):
    model = PassphraseHash


class UnclearDetail(DetailView):
    model = PassphraseHash


class UnclearThanks(UnclearDetail):
    template_name = 'unclear/passphrasehash_thanks.html'
