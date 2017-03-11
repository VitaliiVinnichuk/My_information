# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table(u'person_info_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')()),
            ('bio', self.gf('django.db.models.fields.TextField')(max_length=250, blank=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('jabber', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('other_contacts', self.gf('django.db.models.fields.TextField')(max_length=250)),
        ))
        db.send_create_signal(u'person_info', ['Person'])

        # Adding model 'RequestLogger'
        db.create_table(u'person_info_requestlogger', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('request_method', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('ip_addr', self.gf('django.db.models.fields.IPAddressField')(max_length=15, blank=True)),
            ('full_path', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('priority', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1, blank=True)),
        ))
        db.send_create_signal(u'person_info', ['RequestLogger'])

        # Adding model 'ModelActionLog'
        db.create_table(u'person_info_modelactionlog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('inst', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('action', self.gf('django.db.models.fields.IntegerField')(max_length=1)),
        ))
        db.send_create_signal(u'person_info', ['ModelActionLog'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table(u'person_info_person')

        # Deleting model 'RequestLogger'
        db.delete_table(u'person_info_requestlogger')

        # Deleting model 'ModelActionLog'
        db.delete_table(u'person_info_modelactionlog')


    models = {
        u'person_info.modelactionlog': {
            'Meta': {'object_name': 'ModelActionLog'},
            'action': ('django.db.models.fields.IntegerField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inst': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'person_info.person': {
            'Meta': {'object_name': 'Person'},
            'bio': ('django.db.models.fields.TextField', [], {'max_length': '250', 'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {'max_length': '250'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'person_info.requestlogger': {
            'Meta': {'object_name': 'RequestLogger'},
            'full_path': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_addr': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'blank': 'True'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1', 'blank': 'True'}),
            'request_method': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['person_info']