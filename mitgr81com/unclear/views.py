import string

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Context, loader

from unclear.forms import UnclearForm


def index(request):
    if request.POST:
        form = UnclearForm(request.POST)
        if form.is_valid():
            print form.cleaned_data
            import random
            slug = ''.join([random.choice(string.ascii_letters + string.digits + '-_') for ch in range(8)])
            # verify slug does not exist
            return redirect('/unclear/{}'.format(slug))
    return render(request, 'unclear.html', {'form': UnclearForm()})

def get(request, pass_id):
    print pass_id
    return render(request, 'unclear.html', {'pass_id': pass_id})