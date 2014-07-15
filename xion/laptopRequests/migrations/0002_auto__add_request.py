# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'request'
        db.create_table(u'laptopRequests_request', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('notify', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('readyby', self.gf('django.db.models.fields.DateTimeField')()),
            ('nlaptops', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('experimentName', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('experimentNumber', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal(u'laptopRequests', ['request'])


    def backwards(self, orm):
        # Deleting model 'request'
        db.delete_table(u'laptopRequests_request')


    models = {
        u'laptopRequests.request': {
            'Meta': {'object_name': 'request'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'experimentName': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'experimentNumber': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'nlaptops': ('django.db.models.fields.SmallIntegerField', [], {}),
            'notify': ('django.db.models.fields.SmallIntegerField', [], {}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'readyby': ('django.db.models.fields.DateTimeField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        }
    }

    complete_apps = ['laptopRequests']