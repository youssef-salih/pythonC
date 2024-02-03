from django.shortcuts import render



def index_project (request):
    return render(request, 'base.html')
