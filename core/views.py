from django.shortcuts import render
from django.views.generic.base import TemplateView 
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
import core.models as coremodels


# Landing Page for Index

class LandingView(TemplateView):
	template_name = "blog/index.html"



# Template for About, Blog, StartProject

class BasicView(TemplateView):
	template_name = "themes/basic.html"

class BlogView(ListView):
	model = coremodels.Post
	template_name = "blog/blog.html"

class AboutView(ListView):
	model = coremodels.Post
	template_name = "blog/about.html"

# class StartProjectView(ListView):
# 	model = coremodels.Post
# 	template_name = "blog/startproject.html"
