from django.conf.urls import url
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

from .views import (
				home,
                connexion,
                deconnexion,
				
	)



urlpatterns = [
   
               # url(r'^home/$', home, name="home"),

                url(r'^logout/$', deconnexion, name="logout"),


                #url(r'^register/$', register, name="register"),

                #url(r'^qlq/$', qlq, name="qlq"),

                #url(r'^connexion/$', connexion, name="connexion"),


                #url(r'^update/$', update_user, name="update_user"),

               # url(r'^change_password/$', change_password, name="change_password"),

                #url(r'^reset-password/$', password_reset, name="reset_password"),
                #url(r'^reset-password/done/$', password_reset_done, name="password_reset_done"),

                #url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, name="password_reset_confirm"),

               # url(r'^reset-password/complete/$', password_reset_complete, name="password_reset_complete"),





]