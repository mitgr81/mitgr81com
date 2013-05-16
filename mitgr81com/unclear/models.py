from django.db import models
from django.core.urlresolvers import reverse


class PassphraseHash(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    expire_at = models.DateTimeField(auto_now=True, editable=False)
    passphrase = models.CharField(max_length=64)
    unlock_phrase = models.CharField(max_length=64)
    slug = models.SlugField(max_length=255, blank=True, default='', editable=False)
    max_access = models.IntegerField(default=1)
    access_count = models.IntegerField(default=0, editable=False)

    def get_absolute_url(self):
        return reverse('unclear_thanks', args=[self.slug])
