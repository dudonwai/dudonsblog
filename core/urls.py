from django.conf.urls import patterns, include, url
import core.views as coreviews

urlpatterns = patterns('',

    url(r'^$', coreviews.LandingView.as_view()),
    # url(r'^about', coreviews.AboutView.as_view()),
    url(r'^blog', coreviews.BlogView.as_view()),
    url(r'^startproject', coreviews.StartProjectView.as_view()),
)
