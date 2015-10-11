from django.shortcuts import render
from django.views.generic.base import TemplateView 
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
import core.models as coremodels


# Create your views here.

class BlogView(TemplateView):
	template_name = "blog/index.html"

class PostListView(ListView):
	template_name = "blog/list.html"

class PostDetailView(DetailView):
	model = coremodels.Post
	template_name = "post/20150930.html"
