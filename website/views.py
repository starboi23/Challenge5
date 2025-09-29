from django.http import HttpResponse
from django.shortcuts import render

from hobbies.models import Hobby
from portfolios.models import Portfolio

def welcome(request):
    return render(request, "website/welcome.html")


def contact(request):
    return HttpResponse("Student Email Address: jakeerickson@mail.weber.edu")

def hobby(request):
    return render(request, "website/hobby.html",
                  {"hobbies": Hobby.objects.all()})

def portfolio(request):
    return render(request, "website/portfolio.html",
                  {"portfolios": Portfolio.objects.all()})
