from django.shortcuts import render
from django.http import HttpResponse
from .models import Page
from django.shortcuts import render, get_object_or_404


def index_pages(request, pagename):
    pagename = '/' + pagename
    pg = get_object_or_404(Page, permalink=pagename)

    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'last_updated': pg.updatedate,
        'page_list': Page.objects.all(),
    }
    # assert False
    return render(request, 'pages/page.html', context)
