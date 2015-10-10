from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
import core.views as coreviews

urlpatterns = patterns('',

    url(r'^$', coreviews.BlogView.as_view()),
    url(r'^post/list.html', coreviews.PostListView.as_view()),
    url(r'^post/(?P<pk>\d+)/detail/$', coreviews.PostDetailView.as_view(), name='location_list'),

)


