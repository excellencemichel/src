from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 

from django.views.generic import DetailView, ListView
from .models import TutorialSeries, Lesson

# Create your views here.


# class TutorialSeriesListView(ListView):
# 	model = TutorialSeries


def tutorial_series_list(request):
	""" 
	La fonction prefetch_related permet d'optimiser l'accès à la base de donnée
	Cela vient du fait que lors de la relation ForeignKey dans le model "Lesson" 
	on a indiqué 'related_name' à tutorials, donc ici une requète par en base de
	elle recupère non seulement les tutorials mais aussi les models qui sont liés
	à ce model, ici nous avons profité pour recupérer le model Lesson qui est lié
	par ForeignKey à TutorialsSerie avec related_name: "tutorials", et ce une fois
	seulement.
	annotate permet des recherche en base de donnée, ici à on  fait la recherche
	en base de donnée pour recupérer les leçons lié au model TutorialSeries.
	"""
	tutorials = TutorialSeries.objects.all().prefetch_related(
		"tutorials"
		).annotate(
		lesson=Count("tutorials")
		)



	paginator = Paginator(tutorials, 3)
	page = request.GET.get("page")

	try:
		items = paginator.page(page)
	except PageNotAnInteger:
		items = paginator.page(1)
	except EmptyPage:
		items = paginator.page(paginator.num_pages)

	index = items.number - 1
	max_index = len(paginator.page_range)
	start_index = index - 5 if index >= 5 else 0
	end_index = index + 5 if index <= 5 else max_index
	page_range = paginator.page_range[start_index:end_index]




	context = {
	    "tutorials": tutorials,
	    "items":items,
	    "page_range":page_range,

	}


	return render(request, "tutorials/tutorialseries_list.html", context)


def tutorial_series_detail(request, slug=None):
	series = get_object_or_404(TutorialSeries, slug=slug)
	lessons = series.tutorials.filter(tutorial_series=series)


	context = {
	  "series":series,
	  "lessons":lessons,
	}

	return render(request, "tutorials/tutorial_series_detail.html", context)



# class LessonDetailView(DetailView):
# 	model = Lesson

# 	def get_object(self, tutorial_series, slug):
# 		tutorial_series = TutorialSeries.objects.filter(slug=tutorial_series).first()
# 		object = get_object_or_404(Lesson, tutorial_series=tutorial_series, slug=slug)
# 		return object


# 	def get(self, request, tutorial_series, slug):
# 		self.object = self.get_object(tutorial_series, slug)
# 		context = self.get_context_data(object=self.object)
# 		return self.render_to_response(context)




def lesson_detail(request, tutorial_series, slug):
	lesson = get_object_or_404(Lesson.objects.filter(tutorial_series__slug=tutorial_series,slug=slug))

	context = {
	    "lesson":lesson,
	}

	return render(request, "tutorials/lesson_detail.html", context)



# class TutorialSeriesDetailView(DetailView):
# 	model = TutorialSeries
# 	template = "tutorials/tutorial_series_detail.html"

# 	def get_context_data(self, **kwargs):
# 		context = super(TutorialSeriesDetailView, self).get_context_data(**kwargs)
# 		return context
