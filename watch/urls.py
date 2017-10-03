from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from .views import (
    IndexView,
    WatchList,
    DetailList,
    filter,
    InventoryByUserListView,
    WatchDelete,
    WatchCreate,
    WatchEdit,
    signup
)

app_name = 'watch'

urlpatterns = [
    # /watch/
    url(r'^$', IndexView, name='index'),
    url(r'^watch/$', WatchList, name='watch'),
    url(r'^watch/(?P<pk>[0-9]+)$', DetailList.as_view(), name='detail'),
    url(r'^search/$', filter),
    url(r'^watch/inventory/$', InventoryByUserListView.as_view(), name='inventory'),
    url(r'^watch/(?P<pk>[0-9]+)/delete/$', WatchDelete.as_view(), name='entry-delete'),
    url(r'^watch/create$', WatchCreate, name='create-watch'),
    url(r'^watch/(?P<pk>[0-9]+)/edit/$', WatchEdit.as_view(), name="edit-user-profile"),
]
