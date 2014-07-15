# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'request.status'
        db.alter_column(u'laptopRequests_request', 'status', self.gf('django.db.models.fields.IntegerField')(max_length=1))

        # Changing field 'request.readyby'
        db.alter_column(u'laptopRequests_request', 'readyby', self.gf('django.db.models.fields.DateField')())

        # Changing field 'request.date'
        db.alter_column(u'laptopRequests_request', 'date', self.gf('django.db.models.fields.DateField')())

    def backwards(self, orm):

        # Changing field 'request.status'
        db.alter_column(u'laptopRequests_request', 'status', self.gf('django.db.models.fields.CharField')(max_length=1))

        # Changing field 'request.readyby'
        db.alter_column(u'laptopRequests_request', 'readyby', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'request.date'
        db.alter_column(u'laptopRequests_request', 'date', self.gf('django.db.models.fields.DateTimeField')())

    models = {
        u'laptopRequests.request': {
            'Meta': {'object_name': 'request'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'experimentName': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'experimentNumber': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'nlaptops': ('django.db.models.fields.SmallIntegerField', [], {}),
            'notify': ('django.db.models.fields.SmallIntegerField', [], {}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'readyby': ('django.db.models.fields.DateField', [], {}),
            'status': ('django.db.models.fields.IntegerField', [], {'max_length': '1'})
        }
    }

    complete_apps = ['laptopRequests']