'''from django.http import HttpResponse
from django.template import loader


def start_page(request):
    template = loader.get_template('default.html')
    context = {}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)*/'''

from django.shortcuts import render

def start_page(request):
    return render(request, 'default.html')