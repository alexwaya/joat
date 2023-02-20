from django.shortcuts import render
from accounts.models import Profile


def home(fuck):
    return render(fuck, 'pages/home.html')


def all_members(request):
    members = Profile.objects.all()
    context = {
        "members": members,
    }
    return render(request, 'pages/all_members.html', context)

