# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Recipe.instructions'
        db.delete_column(u'public_recipe', 'instructions')

        # Adding field 'Recipe.Directions'
        db.add_column(u'public_recipe', 'Directions',
                      self.gf('django.db.models.fields.TextField')(default='To be done later.'),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Recipe.instructions'
        db.add_column(u'public_recipe', 'instructions',
                      self.gf('django.db.models.fields.TextField')(default='To be done later.'),
                      keep_default=False)

        # Deleting field 'Recipe.Directions'
        db.delete_column(u'public_recipe', 'Directions')


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
            'Directions': ('django.db.models.fields.TextField', [], {'default': "'To be done later.'"}),
            'Meta': {'object_name': 'Recipe'},
            'description': ('django.db.models.fields.TextField', [], {'default': "'To be done later.'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'default': "'no image'", 'max_length': '500'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['public.Ingredient']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['public']