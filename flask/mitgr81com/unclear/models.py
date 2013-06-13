import binascii
from datetime import datetime
import random
import string

from Crypto.Cipher import AES
from Crypto import Random

from mitgr81com import db
from mitgr81com import app
from . import qaes

class myModel(object):

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def save(self):
        db.session.add(self)
        db.session.commit()


class PassphraseHash(db.Model, myModel):

    def __init__(self, passphrase, max_access):
        self.passphrase = passphrase
        self.max_access = max_access
        super(PassphraseHash, self).__init__()

    __tablename__ = 'unclear_passphrasehash'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    expire_at = db.Column(db.DateTime, default=datetime.now)
    passphrase = db.Column(db.String(255))
    iv = db.Column(db.String(255))
    slug = db.Column(db.String(255))
    max_access = db.Column(db.Integer, default=1)
    access_count = db.Column(db.Integer, default=0)

    class Meta:
        verbose_name_plural = "Passphrase Hashes"

    def __unicode__(self):
        return self.slug

    def __repr__(self):
        return '<Passphrase %r>' % self.slug

    @property
    def remaining_unlocks(self):
        return self.max_access - self.access_count

    @property
    def decry_passphrase(self):
        return qaes.decrypt(self.slug + app.config['SECRET_KEY'][:8], self.passphrase, binascii.a2b_base64(self.iv))


    def save(self, *args, **kwargs):
        if self.id is None:  # Doing an insert
            self.slug = u''.join([random.choice(string.ascii_letters + string.digits + '-_') for ch in range(8)])
            iv = Random.new().read(AES.block_size)
            self.iv = binascii.b2a_base64(iv)
            self.passphrase = qaes.encrypt(self.slug + app.config['SECRET_KEY'][:8], self.passphrase, iv)
        if self.access_count >= self.max_access:
            self.delete()
            return
        super(PassphraseHash, self).save(*args, **kwargs)
