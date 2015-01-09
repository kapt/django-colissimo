# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Rate', fields ['region', 'recommanded', 'weight']
        db.delete_unique(u'colissimo_rate', ['region_id', 'recommanded_id', 'weight'])


        # Changing field 'Recommanded.level'
        db.alter_column(u'colissimo_recommanded', 'level', self.gf('django.db.models.fields.CharField')(unique=True, max_length=4))

    def backwards(self, orm):
        # Adding unique constraint on 'Rate', fields ['region', 'recommanded', 'weight']
        db.create_unique(u'colissimo_rate', ['region_id', 'recommanded_id', 'weight'])


        # Changing field 'Recommanded.level'
        db.alter_column(u'colissimo_recommanded', 'level', self.gf('django.db.models.fields.CharField')(max_length=3, unique=True))

    models = {
        u'colissimo.rate': {
            'Meta': {'object_name': 'Rate'},
            'deposit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'recommanded': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['colissimo.Recommanded']"}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['colissimo.Region']"}),
            'signature': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tracking': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'})
        },
        u'colissimo.recommanded': {
            'Meta': {'object_name': 'Recommanded'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '4'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'})
        },
        u'colissimo.region': {
            'Meta': {'object_name': 'Region'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['colissimo']