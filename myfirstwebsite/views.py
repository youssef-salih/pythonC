from django.http import HttpResponse



def index_project (request):
    return HttpResponse("<h1 style='text-align:center'>bienvenue au site GLWA M2</h1>")
