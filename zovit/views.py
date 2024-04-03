from django.shortcuts import render


def index(request):
    return render(request, 'zovit/index.html')


def contact(request):
    return render(request, 'zovit/contact.html')
