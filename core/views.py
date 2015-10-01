from django.shortcuts import render
from django.views.generic.base import TemplateView 
from django.views.generic.detail import DetailView
import core.models as coremodels


# Create your views here.

class BlogView(TemplateView):
	template_name = "blog/base.html"

class PostView(DetailView):
	model = coremodels.Post
	template_name = "blog/post/20150930.html"


