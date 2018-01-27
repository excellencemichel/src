import datetime
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django.http import HttpResponse
from django.views.generic import View

from .utils import render_to_pdf

from .models import NewsletterUser
from .forms import NewsletterUserSignUpForm

# Create your views here.


def newsletter_signup(request):
	form = NewsletterUserSignUpForm(request.POST or None)

	nom = "Mon nom c'est Excellence Michel"

	if form.is_valid():
		instance = form.save(commit=False)
		if NewsletterUser.objects.filter(email=instance.email).exists():
			messages.warning(request,
			                  "Your email already exist in our datbasease",
			                  "alert alert-warning alert-dismissible")
		else:
			instance.save()
			messages.success(request,
				             "Your email has ben subscribe to the database",
				             "alert alert-success alert-dismissible")
			subject = "Thank you for joining our newsletter"
			from_email = settings.EMAIL_HOST_USER
			to_email = [instance.email]

			with open(settings.BASE_DIR + "/newsletters/templates/newsletters/sign_up_email.txt") as f:
				signup_message = f.read()

			message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email, to=to_email)
			htm_tempale = get_template("newsletters/sign_up_email.html").render()
			message.attach_alternative(htm_tempale, "text/html")
			message.send()


	context = {
	     "form":form,
	     "nom":nom,
	}


	return render(request, "newsletters/sign_up.html", context)


def newletter_unsubscribe(request):
	form = NewsletterUserSignUpForm(request.POST or None)


	if form.is_valid():
		instance = form.save(commit=False)

		if NewsletterUser.objects.filter(email=instance.email).exists():
			NewsletterUser.objects.filter(email=instance.email).delete()
			messages.success(request,
				             "Your email has been removed",
				             "alert alert-success alert-dismissible")


			subject ="You have been unsubscribed"
			from_email = settings.EMAIL_HOST_USER
			global info
			info = "Mes insformation"
			to_email = [instance.email]
			with open(settings.BASE_DIR + "/newsletters/templates/newsletters/unsubscribe_email.txt") as f:
				signup_message = f.read()

			message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email, to=to_email)
			htm_tempale = get_template("newsletters/unsubscribe_email.html").render()
			message.attach_alternative(htm_tempale, "text/html")
			message.send()

		else:
			messages.warning(request,
			 "Your email is not in the database",
             "alert alert-warning alert-dismissible"
                    
			)




	context = {
	    "form":form,
	}

	return render(request, "newsletters/unsubscribe.html", context)



class GeneratePdf(View):
	def get(self, request, *args, **kwargs):
		template = get_template("pdf/invoice.html")
		context = {
				"invoice_id":123,
				"today" : datetime.date.today(),
				"amount" : 39.99,
				"customer_name": "Excellence Michel",
				"order_id": 1233434,
		}
		html = template.render(context)

		pdf = render_to_pdf("pdf/invoice.html", context)
		if pdf:
			response=HttpResponse(pdf, content_type="application/pdf")
			filename = "Invoice_%s.pdf" %("12341231")
			content = "inline; filename='%s'" %(filename)
			download = request.GET.get("download")
			if download:
				content = "attachement; filename='%s'"%(filename)
			response["Content-Disposition"] = content
			return response
		return HttpResponse("Not found")