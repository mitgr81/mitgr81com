# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'PassphraseHash.iv'
        db.alter_column(u'unclear_passphrasehash', 'iv', self.gf('django.db.models.fields.CharField')(max_length=255))

    def backwards(self, orm):

        # Changing field 'PassphraseHash.iv'
        db.alter_column(u'unclear_passphrasehash', 'iv', self.gf('django.db.models.fields.CharField')(max_length=16))

    models = {
        u'unclear.passphrasehash': {
            'Meta': {'object_name': 'PassphraseHash'},
            'access_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'expire_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iv': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'max_access': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'passphrase': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "''", 'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['unclear']