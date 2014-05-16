from django.conf.urls import patterns, include, url

urlpatterns = patterns('user_profile.views',
    url(r'^home$', 'home', name='user_profile_home'))