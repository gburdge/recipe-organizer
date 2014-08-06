from django.conf.urls import patterns, include, url
from apps.public.views import *
from django.contrib import admin
from rest_framework import routers

admin.autodiscover()

router = routers.DefaultRouter()
# router.register(r'recipes', RecipeViewSet)
# router.register(r'ingredients', IngredientViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^recipes$', RecipeList.as_view(), name='recipe-list'),
    url(r'^recipes/(?P<pk>[0-9]+$)', RecipeDetail.as_view(), name='recipe-list')
)

