from django.conf.urls import patterns, include, url
import core.views as coreviews




urlpatterns = patterns('',

    url(r'^$', coreviews.BlogView.as_view()),
    url(r'^post/list.html', coreviews.PostListView.as_view()),
    url(r'^blog/20150930.html', coreviews.Blog20150930View.as_view()),

)
