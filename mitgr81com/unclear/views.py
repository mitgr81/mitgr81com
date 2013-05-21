from django.views.generic import CreateView, DetailView, ListView

from .models import PassphraseHash


class UnclearList(ListView):
    model = PassphraseHash


class UnclearCreate(CreateView):
    model = PassphraseHash


class UnclearDetail(DetailView):
    model = PassphraseHash

    # def get_context_data(self, **kwargs):
    #     context = super(UnclearDetail, self).get_context_data(**kwargs)
    #     return context


class UnclearThanks(UnclearDetail):
    template_name = 'unclear/passphrasehash_thanks.html'

    def get_context_data(self, **kwargs):
        context = super(UnclearThanks, self).get_context_data(**kwargs)
        context['full_uri'] = self.request.build_absolute_uri().replace('/created', '')
        return context
