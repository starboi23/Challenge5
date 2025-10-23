from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import PortfolioForm

from portfolios.models import Portfolio

def port_detail(request, id):
    portfolio = get_object_or_404(Portfolio, pk=id)
    return render(request, 'portfolios/port_detail.html', {'portfolio': portfolio})

# Create your views here.

def portfolios_list(request):
    return render(request, "portfolios/portfolios_list.html",
                  {"portfolios": Portfolio.objects.all()})

def portfolio_image_view(request):
    if request.method == "POST":
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PortfolioForm()
    return render(request, 'portfolios/portfolio_image_form.html', {'form': form})

