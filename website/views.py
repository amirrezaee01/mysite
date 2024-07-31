from django.shortcuts import render
from django.http import HttpResponse
from website.models import Contact
from website.forms import Nameform,ContactForm,NewsletterForm

def index_view(request):
    return render(request, 'website/index.html')
def about_view(request):
    return render(request, 'website/about.html')
def contact_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return HttpResponse('you have problem')
    form = ContactForm()
    return render(request, 'website/contact.html', {'form':form})
def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
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