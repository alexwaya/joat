from django.shortcuts import render



def home(fuck):
    return render(fuck, 'pages/home.html')