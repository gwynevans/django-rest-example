# ---- Routers
# ------------
from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers

from items import views
from . import api_views

router = SimpleRouter()
router.register(r'api', api_views.TaskViewSet)  # will define /api/ and /api/<pk>/

location_router = routers.NestedSimpleRouter(router, r'api', lookup='location')
# Will add /api/<locn_pk>/tasks/<task_pk>
location_router.register(r'tasks', api_views.LocationSpecificViewSet)

app_name = "items"

# The API URLs are determined automatically by the routers.
urlpatterns = [
    # Deliberately not registering base router
    # url(r'^', include(router.urls)),
    url(r'^',  include(location_router.urls)),
    # Web views
    url(r'^$',                 views.LocationListView.as_view(),   name='location-list'),
    url(r'^(?P<pk>\d+)/$',     views.LocationDetailView.as_view(), name='location-detail'),
    url(r'^new/$',             views.LocationCreateView.as_view(), name='location-create'),
    url(r'^(?P<pk>\d+)/upd/$', views.LocationUpdateView.as_view(), name='location-update'),
]