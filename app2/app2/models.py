import binascii
from datetime import datetime
import random
import string

from Crypto.Cipher import AES
from Crypto import Random

from mitgr81com.database import db

class myModel(object):

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def save(self):
        db.session.add(self)
        db.session.commit()


class TestModel(db.Model, myModel):

    def __init__(self, passphrase):
        self.passphrase = passphrase
        super(TestModel, self).__init__()

    __tablename__ = 'test_table'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    expire_at = db.Column(db.DateTime, default=datetime.now)
    passphrase = db.Column(db.String(255))
    iv = db.Column(db.String(255))
    slug = db.Column(db.String(255))
    max_access = db.Column(db.Integer, default=1)
    access_count = db.Column(db.Integer, default=0)

    def __unicode__(self):
        return self.slug

    def __repr__(self):
        return '<TestModel %r>' % self.slug

    @property
    def remaining_unlocks(self):
        return self.max_access - self.access_count

    def save(self, *args, **kwargs):
        if self.id is None:  # Doing an insert
            self.max_access = 4
            self.slug = u''.join([random.choice(string.ascii_letters + string.digits + '-_') for ch in range(8)])
            iv = Random.new().read(AES.block_size)
            self.iv = binascii.b2a_base64(iv)
        if self.access_count >= self.max_access:
            self.delete()
            return
        super(TestModel, self).save(*args, **kwargs)
