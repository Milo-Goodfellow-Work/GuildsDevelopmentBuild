
"""Guilds URL Configurationfrom django import forms


The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#Non project imports
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500
from django.views.generic import TemplateView

#Project imports
from Guilds import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    #Beginning of added URLS
    path('UserEntry/', include('UserEntry.urls')),
    path('UserProfiles/', include('UserProfiles.urls')),
    path('LaunchGuild/', include('GuildCreation.urls')),
    path('GuildProfiles/', include('GuildProfiles.urls')),
    path('GuildPost/', include('GuildPosts.urls')),
    path('UserPost/', include('UserPosts.urls')),
    path('Follow/', include('Follow.urls')),
    path('Home', include('Home.urls')),
    path('UserSettings/', include('UserSettings.urls')),
    path('Search/', include('FullSearch.urls')),
    path('404test/', TemplateView.as_view(template_name='404.html')),
    path('Discover/', include('Discover.urls')),
    path('GroupChat/', include('GroupChat.urls')),
    path('Notifications/', include('Notifications.urls')),
    path('Logout/', include('UserLogout.urls')),
    path('Group', include('GroupPage.urls'))

]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
