from django.conf.urls import url

from .views import newsletter_signup, newletter_unsubscribe


urlpatterns = [
        
        url(r'^sign_up/$', newsletter_signup, name="newsletter_signup"),
        url(r'^unsubscribe/$', newletter_unsubscribe, name="newletter_unsubscribe"),

 
         ]