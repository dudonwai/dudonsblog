from django.shortcuts import render
from django.views.generic.base import TemplateView 
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
import core.models as coremodels


# Landing Page for Index

class LandingView(TemplateView):
	template_name = "blog/index.html"



# Template for About, Archive, Contact

class BasicView(TemplateView):
	template_name = "themes/basic.html"

class BlogView(ListView):
	model = coremodels.Post
	template_name = "blog/20151025-education.html"



# Blog Posts

class Blog20150930View(TemplateView):
    model = coremodels.Post
    template_name = 'blog/20150930-whyblog.html'
