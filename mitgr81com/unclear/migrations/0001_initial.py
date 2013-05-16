# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PassphraseHash'
        db.create_table(u'unclear_passphrasehash', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('expire_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('passphrase', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('unlock_phrase', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('slug', self.gf('django.db.models.fields.SlugField')(default='', max_length=255, blank=True)),
            ('max_access', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('access_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'unclear', ['PassphraseHash'])


    def backwards(self, orm):
        # Deleting model 'PassphraseHash'
        db.delete_table(u'unclear_passphrasehash')


    models = {
        u'unclear.passphrasehash': {
            'Meta': {'object_name': 'PassphraseHash'},
            'access_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'expire_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_access': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'passphrase': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'unlock_phrase': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['unclear']