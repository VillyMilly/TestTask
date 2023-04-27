from django.shortcuts import render
from protomodels.models import Data


def start_page(request):
    if request.method == "GET":  # suitability check request
        if request.GET.__contains__('data'):  # checking for the presence of a parameter 'data'
            a = Data.objects.create(data=request.GET.__getitem__('data'))
    return render(request, 'default.html')
