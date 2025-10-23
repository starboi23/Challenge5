from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import HobbyForm

from hobbies.models import Hobby

def detail(request, id):
    hobby = get_object_or_404(Hobby, pk=id)
    return render(request, "hobbies/detail.html", {"hobby": hobby})

def hobbies_list(request):
    return render(request, "hobbies/hobbies_list.html",
                  {"hobbies": Hobby.objects.all()})

def hobby_image_view(request):
    if request.method == "POST":
        form = HobbyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = HobbyForm()
    return render(request, 'hobbies/hobby_image_form.html', {'form': form})

def success(request):
    return HttpResponse('successfully uploaded')


