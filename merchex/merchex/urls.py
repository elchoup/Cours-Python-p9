"""
URL configuration for merchex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bands/', views.band_list, name='band_list'),
    path('bands/<int:band_id>/', views.band_detail, name='band_detail'),
    path('bands/add/', views.band_create, name='band-create'),
    path('bands/<int:band_id>/change', views.band_change, name='band-change'),
    path('bands/<int:band_id>/delete', views.band_delete, name= 'band-delete'),
    path('about-us/', views.about, name='about'),
    path('listings/', views.listings, name='listings'),
    path('listings/<int:listing_id>', views.listing_detail, name='listing_detail'),
    path('listings/add', views.listing_create, name='listing-create'),
    path('listings/<int:listing_id>/change', views.listing_change, name = 'listing-change'),
    path('listings/<int:listing_id>/delete', views.listing_delete, name = 'listing-delete'),
    path('contact-us/', views.contact, name='contact'),
    path('contact-us/email-validation/', views.email_validation, name='email-validation'),
]
