"""
URL configuration for PortfolioDatabase project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from PortfolioDatabase import settings
from website import views
from website.views import welcome, contact, hobby, portfolio
from hobbies.views import detail, hobbies_list, hobby_image_view, success
from portfolios.views import port_detail, portfolios_list, portfolio_image_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome),
    path('contact', contact),
    path('hobbies/<int:id>', detail),
    path('hobbies', hobbies_list, name='hobbies'),

    path('portfolios', portfolios_list),
    path('hobbies/<int:id>', detail),
    path('portfolios/<int:id>', port_detail),

    path('hobby_image_upload/', hobby_image_view, name='image_upload'),
    path('portfolio_image_upload/', portfolio_image_view),
    path('success/', success, name='success'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
