from django.conf import settings
from django.contrib import messages
from django.shortcuts import render
from django.core.mail import send_mail

from .models import NewsletterUser
from .forms import NewsletterUserSignUpForm

# Create your views here.


def newsletter_signup(request):
	form = NewsletterUserSignUpForm(request.POST or None)

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
			signup_message = """Welcom to Master code online newsletter. If you would like to unsubcribe visit http://127.0.0.1:8000/newsletter/unsubscribe"""
			send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=signup_message, fail_silently=False)


	context = {
	     "form":form,
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
		to_email = [instance.email]
		signup_message = """Sorry to see you go let us know if an issue with our service"""
		send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=signup_message, fail_silently=False)



	else:
		messages.warning(request,
			 "Your email is not in the database",
             "alert alert-warning alert-dismissible"
                    
			)




	context = {
	    "form":form,
	}

	return render(request, "newsletters/unsubscribe.html", context)


