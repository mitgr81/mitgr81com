from django.views.generic import CreateView, ListView, DetailView
from django.http import HttpResponse

from .models import PassphraseHash


class UnclearList(ListView):
    model = PassphraseHash


class UnclearCreate(CreateView):
    model = PassphraseHash


class UnclearDetail(DetailView):
    model = PassphraseHash
    http_method_names = ['get', 'patch']

    def patch(self, request, *args, **kwargs):
        if 'decrypted' in request.body:  # should really json load this
            this_hash = PassphraseHash.objects.get(slug=kwargs['slug'])
            this_hash.access_count += 1
            this_hash.save()

            return HttpResponse("okay!", content_type="application/json")
        return HttpResponse("Nope", status=403)


class UnclearThanks(UnclearDetail):
    template_name = 'unclear/passphrasehash_thanks.html'

    def get_context_data(self, **kwargs):
        context = super(UnclearThanks, self).get_context_data(**kwargs)
        context['full_uri'] = self.request.build_absolute_uri().replace('/created', '')
        return context
