# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Region'
        db.create_table(u'colissimo_region', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'colissimo', ['Region'])

        # Adding model 'Recommanded'
        db.create_table(u'colissimo_recommanded', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('level', self.gf('django.db.models.fields.CharField')(unique=True, max_length=3)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
        ))
        db.send_create_signal(u'colissimo', ['Recommanded'])

        # Adding model 'Rate'
        db.create_table(u'colissimo_rate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('weight', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('signature', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('deposit', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tracking', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['colissimo.Region'])),
            ('recommanded', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['colissimo.Recommanded'])),
        ))
        db.send_create_signal(u'colissimo', ['Rate'])

        # Adding unique constraint on 'Rate', fields ['weight', 'region', 'recommanded']
        db.create_unique(u'colissimo_rate', ['weight', 'region_id', 'recommanded_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Rate', fields ['weight', 'region', 'recommanded']
        db.delete_unique(u'colissimo_rate', ['weight', 'region_id', 'recommanded_id'])

        # Deleting model 'Region'
        db.delete_table(u'colissimo_region')

        # Deleting model 'Recommanded'
        db.delete_table(u'colissimo_recommanded')

        # Deleting model 'Rate'
        db.delete_table(u'colissimo_rate')


    models = {
        u'colissimo.rate': {
            'Meta': {'unique_together': "((u'weight', 'region', 'recommanded'),)", 'object_name': 'Rate'},
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
            'level': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'})
        },
        u'colissimo.region': {
            'Meta': {'object_name': 'Region'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['colissimo']