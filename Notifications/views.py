from django.shortcuts import render

from .models import Notification

# Create your views here.
def Notifications(request):
    NotificationLi = Notification.objects.filter(UserNotify = request.user)
    return render(request, 'Notifications/Notifications.html', {'NotificationLi':NotificationLi, 'Username':request.user.username})
