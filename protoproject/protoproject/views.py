from django.shortcuts import render, redirect
from protomodels.models import Data


def start_page(request):
    if request.GET.__contains__('id'):
        id_obj = request.GET['id']
        if id_obj:
            print(id)
            data_obj = Data.objects.get(pk=id_obj).data
            return render(request, 'idpage.html', {'data': data_obj})
    return render(request, 'default.html')


def id_page(request):
    data = request.POST['data']
    if data:
        Data.objects.create(data=data)
    else:
        return redirect('start_page')
    return render(request, 'idpage.html', {'data': data})
