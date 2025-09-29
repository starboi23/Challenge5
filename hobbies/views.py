from django.shortcuts import render, get_object_or_404

from hobbies.models import Hobby

def detail(request, id):
    hobby = get_object_or_404(Hobby, pk=id)
    return render(request, "hobbies/detail.html", {"hobby": hobby})
