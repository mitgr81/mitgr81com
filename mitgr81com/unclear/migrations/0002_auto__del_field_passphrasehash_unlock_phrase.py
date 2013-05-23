# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'PassphraseHash.unlock_phrase'
        db.delete_column(u'unclear_passphrasehash', 'unlock_phrase')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'PassphraseHash.unlock_phrase'
        raise RuntimeError("Cannot reverse this migration. 'PassphraseHash.unlock_phrase' and its values cannot be restored.")

    models = {
        u'unclear.passphrasehash': {
            'Meta': {'object_name': 'PassphraseHash'},
            'access_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'expire_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_access': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'passphrase': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "''", 'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['unclear']