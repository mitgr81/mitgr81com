import random
import string

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from Crypto.Cipher import AES
from Crypto import Random

from unclear import qaes


class PassphraseHash(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    expire_at = models.DateTimeField(auto_now=True, editable=False)
    passphrase = models.CharField(max_length=255)
    iv = models.CharField(max_length=16, editable=False)
    slug = models.SlugField(max_length=255, blank=True, default='', editable=False)
    max_access = models.IntegerField(default=1)
    access_count = models.IntegerField(default=0, editable=False)

    class Meta:
        verbose_name_plural = "Passphrase Hashes"

    def __unicode__(self):
        return self.slug

    @property
    def remaining_unlocks(self):
        return self.max_access - self.access_count

    @property
    def decry_passphrase(self):
        return self.passphrase
        return qaes.decrypt(self.passphrase, self.iv)

    def get_absolute_url(self):
        return reverse('unclear_thanks', args=[self.slug])

    def save(self, *args, **kwargs):
        if self.pk is None:  # Doing an insert
            self.slug = u''.join([random.choice(string.ascii_letters + string.digits + '-_') for ch in range(8)])
            self.iv = Random.new().read(AES.block_size)
            # import pdb; pdb.set_trace()
            self.passphrase = unicode(qaes.encrypt(self.slug + settings.SECRET_KEY[:8], self.passphrase, self.iv))
            print self.passphrase
        super(PassphraseHash, self).save(*args, **kwargs)
