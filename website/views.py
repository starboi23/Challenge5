from django.http import HttpResponse
from django.shortcuts import render

from hobbies.models import Hobby
from portfolios.models import Portfolio

links = [
    {"name": "Contact", "path": "/contact"},
    {"name": "Top Stories API", "path": "/anotherpage"},
    {"name": "Most Popular API", "path": "/popular"},
    {"name": "Times Wire API", "path": "/feed"} ]

def welcome(request):
    return render(request, "website/welcome.html")


def contact(request):
    return render(request, "website/contact.html", {'title': 'Student Email Address: jakeerickson@mail.weber.edu'})

def hobby(request):
    return render(request, "website/hobby.html",
                  {"hobbies": Hobby.objects.all()})

def portfolio(request):
    return render(request, "website/portfolio.html",
                  {"portfolios": Portfolio.objects.all()})

def anotherpage(request):
    return render(request, 'website/results.html', {'title': 'Student Email Address: jakeerickson@mail.weber.edu', 'subtitle': 'Another Page', 'results': [], 'links': links})
