from django.shortcuts import render


def home(request):
    """
    A index view.
    """
    return render(request, 'DevCafe/index.html')
