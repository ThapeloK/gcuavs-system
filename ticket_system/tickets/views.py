from django.template import loader
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import AV_Request
from .forms import TicketRequestForm

av_requests = [
    {
        'requester':'ThapeloK',
        'title': 'Sound System Hire',
        'content': 'Hiring for alu',
        'date_posted':'August 27,2020',
        'status': 'open'
    },
       {
        'requester':'BenOhp',
        'title': 'TV System Hire',
        'content': 'Hiring for alu',
        'date_posted':'August 28,2020',
        'status': 'closed'
    }
]
@login_required(login_url='login')
def index(request):
    context = {
        'av_requests': av_requests

        #'av_requests': AV_Request.objects.all()
    }
    return render(request, 'tickets/index.html', context)

def ticketform(request):
    form = TicketRequestForm()
    return render(request, 'ticketform.html', {'form':form})
