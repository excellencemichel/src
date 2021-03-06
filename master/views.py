from django.shortcuts import render


from tutorials.models import TutorialSeries


def home(request):
	series = TutorialSeries.objects.filter(archived=False).order_by("-id")
	context = {
	    "series":series,
	}
	return render(request, "home.html", context)