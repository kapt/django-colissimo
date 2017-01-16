# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Recommanded.price'
        db.alter_column(u'colissimo_recommanded', 'price', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2))

    def backwards(self, orm):

        # Changing field 'Recommanded.price'
        db.alter_column(u'colissimo_recommanded', 'price', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2))

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
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'})
        },
        u'colissimo.region': {
            'Meta': {'object_name': 'Region'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['colissimo']