from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, bedroom_choices, state_choices         
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from listings.models import Listing
from realtors.models import Realtor
from about.models import About

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published = True) [:3]

    context = {
        'listings' : listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }

    return render (request, 'pages/index.html', context )

def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')
    paginator = Paginator(realtors, 6)
    page = request.GET.get('page')
    paged_realtors = paginator.get_page(page)
    
    # Get MVP 
    mvp_realtors = Realtor.objects.all().filter(is_mvp = True)

    about = About.objects.all()
    paginator = Paginator(about, 1)
    page = request.GET.get('page')
    paged_about = paginator.get_page(page)

    context= {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors,
        'realtors' : paged_realtors,
        'about' : paged_about
    }
    
    return render (request, 'pages/about.html', context)  