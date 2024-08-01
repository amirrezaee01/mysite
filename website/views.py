from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from website.models import Contact
from django.contrib import messages
from website.forms import Nameform,ContactForm,NewsletterForm

def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.name = 'unknown'
            contact.save()
            messages.add_message(request, messages.SUCCESS, 'Your ticket was submitted correctly.')
        else:
            messages.add_message(request, messages.ERROR, 'Your ticket did not submit correctly.')
    else:
        form = ContactForm()

    return render(request, 'website/contact.html', {'form': form})

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your ticket was submitted correctly.')
            
            return HttpResponseRedirect('/')
        
    else:
        messages.add_message(request, messages.ERROR, 'Your ticket did not submit correctly.')
        
        return HttpResponseRedirect('/')
    
        
    

def test_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save() 
            return HttpResponse ("Done")
        else:
            return HttpResponse ("Not valiid")

    return render(request, 'website/test.html',{'form':form})