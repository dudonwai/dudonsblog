from django.conf.urls import patterns, include, url
import core.views as coreviews

urlpatterns = patterns('',

    url(r'^$', coreviews.LandingView.as_view()),
    url(r'^blog/20150930-whyblog', coreviews.Blog20150930View.as_view()),
	url(r'^blog/20151025-education', coreviews.BlogView.as_view()),
)
