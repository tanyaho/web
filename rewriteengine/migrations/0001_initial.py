# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'htaccess'
        db.create_table(u'rewriteengine_htaccess', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('CMS', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('redirection', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('rewrite', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('rule', self.gf('django.db.models.fields.TextField')()),
            ('condition', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
        ))
        db.send_create_signal(u'rewriteengine', ['htaccess'])


    def backwards(self, orm):
        # Deleting model 'htaccess'
        db.delete_table(u'rewriteengine_htaccess')


    models = {
        u'rewriteengine.htaccess': {
            'CMS': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'Meta': {'object_name': 'htaccess'},
            'condition': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'redirection': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rewrite': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rule': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['rewriteengine']