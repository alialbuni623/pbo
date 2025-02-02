from django.shortcuts import render

def index(request):
    return render(request, 'UAS_PEMROGRAMAN/index.html')
