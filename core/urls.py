from django.conf.urls import patterns, include, url
import core.views as coreviews

urlpatterns = patterns('',

    url(r'^$', 'index', name='index', coreviews.BlogView.as_view()),
    url(r'^post/list.html', coreviews.PostListView.as_view()),
    url(r'^blog/20150930', coreviews.Blog20150930View.as_view()),
)
