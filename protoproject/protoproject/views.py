from django.shortcuts import render, redirect
from protomodels.models import Data
from django.views.generic import DetailView


def start_page(request):
    return render(request, 'default.html')


def redirect_page(request):
    data = request.POST.get('data')
    if data:
        w = Data.objects.create(data=data)
    else:
        return redirect('start_page')
    return redirect('id_page', w.pk)


class IdDetail(DetailView):
    model = Data
    template_name = 'idpage.html'
    context_object_name = 'idtext'
