# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Recipe.image'
        db.delete_column(u'public_recipe', 'image')

        # Adding field 'Recipe.photo'
        db.add_column(u'public_recipe', 'photo',
                      self.gf('django.db.models.fields.CharField')(default='no image', max_length=500),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Recipe.image'
        db.add_column(u'public_recipe', 'image',
                      self.gf('django.db.models.fields.CharField')(default='no image', max_length=500),
                      keep_default=False)

        # Deleting field 'Recipe.photo'
        db.delete_column(u'public_recipe', 'photo')


    models = {
        u'public.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'public.ingredientcategory': {
            'Meta': {'object_name': 'IngredientCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'public.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'description': ('django.db.models.fields.TextField', [], {'default': "'To be done later.'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['public.Ingredient']", 'null': 'True', 'blank': 'True'}),
            'instructions': ('django.db.models.fields.TextField', [], {'default': "'To be done later.'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'photo': ('django.db.models.fields.CharField', [], {'default': "'no image'", 'max_length': '500'})
        }
    }

    complete_apps = ['public']