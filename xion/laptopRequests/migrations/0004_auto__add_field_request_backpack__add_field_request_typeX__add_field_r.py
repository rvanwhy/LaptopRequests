# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'request.backpack'
        db.add_column(u'laptopRequests_request', 'backpack',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'request.typeX'
        db.add_column(u'laptopRequests_request', 'typeX',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=40, blank=True),
                      keep_default=False)

        # Adding field 'request.typeL'
        db.add_column(u'laptopRequests_request', 'typeL',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=40, blank=True),
                      keep_default=False)

        # Adding field 'request.owner'
        db.add_column(u'laptopRequests_request', 'owner',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=40, blank=True),
                      keep_default=False)

        # Adding field 'request.ninstr'
        db.add_column(u'laptopRequests_request', 'ninstr',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'request.diskspace'
        db.add_column(u'laptopRequests_request', 'diskspace',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=40),
                      keep_default=False)

        # Adding field 'request.media'
        db.add_column(u'laptopRequests_request', 'media',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=40),
                      keep_default=False)

        # Adding field 'request.software'
        db.add_column(u'laptopRequests_request', 'software',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=40),
                      keep_default=False)

        # Adding field 'request.notes'
        db.add_column(u'laptopRequests_request', 'notes',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


        # Changing field 'request.status'
        db.alter_column(u'laptopRequests_request', 'status', self.gf('django.db.models.fields.CharField')(max_length=40))

        # Changing field 'request.notify'
        db.alter_column(u'laptopRequests_request', 'notify', self.gf('django.db.models.fields.BooleanField')())

    def backwards(self, orm):
        # Deleting field 'request.backpack'
        db.delete_column(u'laptopRequests_request', 'backpack')

        # Deleting field 'request.typeX'
        db.delete_column(u'laptopRequests_request', 'typeX')

        # Deleting field 'request.typeL'
        db.delete_column(u'laptopRequests_request', 'typeL')

        # Deleting field 'request.owner'
        db.delete_column(u'laptopRequests_request', 'owner')

        # Deleting field 'request.ninstr'
        db.delete_column(u'laptopRequests_request', 'ninstr')

        # Deleting field 'request.diskspace'
        db.delete_column(u'laptopRequests_request', 'diskspace')

        # Deleting field 'request.media'
        db.delete_column(u'laptopRequests_request', 'media')

        # Deleting field 'request.software'
        db.delete_column(u'laptopRequests_request', 'software')

        # Deleting field 'request.notes'
        db.delete_column(u'laptopRequests_request', 'notes')


        # Changing field 'request.status'
        db.alter_column(u'laptopRequests_request', 'status', self.gf('django.db.models.fields.IntegerField')(max_length=1))

        # Changing field 'request.notify'
        db.alter_column(u'laptopRequests_request', 'notify', self.gf('django.db.models.fields.SmallIntegerField')())

    models = {
        u'laptopRequests.request': {
            'Meta': {'object_name': 'request'},
            'backpack': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'diskspace': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'experimentName': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'experimentNumber': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'media': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'ninstr': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'nlaptops': ('django.db.models.fields.SmallIntegerField', [], {}),
            'notes': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'notify': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'readyby': ('django.db.models.fields.DateField', [], {}),
            'software': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'typeL': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'typeX': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'})
        }
    }

    complete_apps = ['laptopRequests']