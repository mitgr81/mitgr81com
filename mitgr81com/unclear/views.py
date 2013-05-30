from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .models import PassphraseHash


class UnclearList(ListView):
    model = PassphraseHash


class UnclearCreate(CreateView):
    model = PassphraseHash

class UnclearDetail(UpdateView):
    model = PassphraseHash
    template_name = 'unclear/passphrasehash_detail.html'

    # def get_context_data(self, **kwargs):
    #     context = super(UnclearDetail, self).get_context_data(**kwargs)
    #     import pdb; pdb.set_trace()
    #     return context

    def put(self, request, *args, **kwargs):
        import pdb; pdb.set_trace()

    def patch(self, *args, **kwargs):
        import pdb; pdb.set_trace()


class UnclearThanks(UnclearDetail):
    template_name = 'unclear/passphrasehash_thanks.html'

    def get_context_data(self, **kwargs):
        context = super(UnclearThanks, self).get_context_data(**kwargs)
        context['full_uri'] = self.request.build_absolute_uri().replace('/created', '')
        return context
