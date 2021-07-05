from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Notifications_Reciver.models import Service
from users.models import Profile


@csrf_exempt
def home(request):
    context = {'services': Service.objects.all()}

    return render(request, 'notifications/home.html', context)


def about(request):

    return render(request, 'notifications/about.html', {'title': 'About'})
