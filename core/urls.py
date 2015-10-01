from django.conf.urls import include, url
import core.views as coreviews

urlpatterns = [
    url(r'^$', coreviews.BlogView.as_view()),
    url(r'^post/$', coreviews.PostView)
]
