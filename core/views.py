from django.shortcuts import render
from django.views.generic.base import TemplateView 
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
import core.models as coremodels
from django.views.generic.edit import CreateView, UpdateView
from sitegate.decorators import redirect_signedin, sitegate_view

# Create your views here.

class LandingView(TemplateView):
	template_name = "base/index.html"

class BlogListView(ListView):
    model = coremodels.Location
    template_name = 'location/list.html'
	

class LocationListView(ListView):
    model = coremodels.Location
    template_name = 'location/list.html'
    paginate_by = 5