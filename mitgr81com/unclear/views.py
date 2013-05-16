import string
import random
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, DetailView
# from django.http import HttpResponse
# from django.template import Context, loader

from .models import PassphraseHash


# def index(request):
#     if request.POST:
#         form = UnclearForm(request.POST)
#         if form.is_valid():
#             print form.cleaned_data
#             import random
#             slug = ''.join([random.choice(string.ascii_letters + string.digits + '-_') for ch in range(8)])
#             # verify slug does not exist
#             return redirect('/unclear/{}'.format(slug))
#     return render(request, 'unclear.html', {'form': UnclearForm()})

# def get(request, pass_id):
#     print pass_id
#     return render(request, 'unclear.html', {'pass_id': pass_id})

class UnclearCreate(CreateView):
    model = PassphraseHash

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.slug = ''.join([random.choice(string.ascii_letters + string.digits + '-_') for ch in range(8)])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class UnclearDetail(DetailView):
    model = PassphraseHash
