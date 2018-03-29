<<<<<<< HEAD
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def home_page(request):
    if request.method == 'POST':
        return HttpResponse(request.POST['item_text'])
    return render(request, 'home.html',
                  {'new_item_text': request.POST['item_text']})
=======
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def home_page(request):
    if request.method == 'POST':
        return HttpResponse(request.POST['item_text'])
    return render(request, 'home.html',
                  {'new_item_text': request.POST['item_text']})
>>>>>>> 978be58aa72e1dfc76afeb677f114895df88544e
