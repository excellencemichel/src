from django.shortcuts import render, get_object_or_404

from django.views.generic import DetailView
from .models import TutorialSeries

# Create your views here.


def tutorial_series_detail(request, slug=None):
	obj = get_object_or_404(TutorialSeries, slug=slug)


	context = {
	  "obj":obj,
	}

	return render(request, "tutorials/tutorial_series_detail.html", context)



# class TutorialSeriesDetailView(DetailView):
# 	model = TutorialSeries
# 	template = "tutorials/tutorial_series_detail.html"

# 	def get_context_data(self, **kwargs):
# 		context = super(TutorialSeriesDetailView, self).get_context_data(**kwargs)
# 		return context
