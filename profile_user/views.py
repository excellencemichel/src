from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.core.urlresolvers import reverse

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash 

from .forms import UserCreationForm, ConnexionForm, ProfileUserChangeForm

# Create your views here.


def home(request):
	return render(request, "profile_user/home.html")



"""
def base(request):
	return render(request, "base.html")

"""
"""
def register(request):
	if request.method=="POST":
		form = UserCreationForm(request.POST or None, request.FILES or None)

		if form.is_valid():
			form.save()
			return redirect(reverse(connexion))


	else :
		form = UserCreationForm()

	context = {
	   "form" : form,
	}


	return render(request, "profile_user/register.html", context)

@login_required
def qlq(request):
	return render(request, "profile_user/qlq.html")
"""
def connexion(request):
	error = False

	if request.method=="POST":
		form = ConnexionForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]


			user = authenticate(username=username, password=password)

			if user:
				login(request, user)
				return redirect(reverse(home))

			else:
				error = True
	else:
		form = ConnexionForm()

	context = {
	    "form": form,
	    "error":error,
	}

	return render(request, "profile_user/home.html",context)

"""
def update_user(request):
	if request.method=="POST":
		form = ProfileUserChangeForm(request.POST or None, request.FILES or None)

		if form.is_valid():
			form.save()
			return redirect(reverse(home))

	else:
		form = ProfileUserChangeForm()


	context = {
	    "form": form,
	}

	return render(request, "profile_user/update_user.html", context)

@login_required
def change_password(request):
	error = False
	if request.method=="POST":
		form = PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect(home)

		else:
			error = True


	else:
		form = PasswordChangeForm(user=request.user)

	context = {
	   "form":form,
	   "error":error,
	}

	return render(request, "profile_user/change_password.html", context)
"""



def deconnexion(request):
	logout(request)
	return redirect(reverse("account_login"))