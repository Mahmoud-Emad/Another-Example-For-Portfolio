from django.shortcuts import render, redirect
from main.forms import ContactForm
from django.urls.base import reverse
from django.contrib import messages
# Create your views here.


def HomeView(request):
    form_contact = ContactForm(request.POST)
    if request.method == 'POST':
        if form_contact.is_valid():
            form = ContactForm(request.POST)
            form.save()
            messages.info(request, "Lot of thank's for you'r time “The e-mail has been received and the test is also received, and your problem will be solved as soon as possible, then a mail will be sent to you with the correct answer Please follow your mail and do not forget to look at the span box” ")
            return redirect(reverse('Home'))
    else:
        form = ContactForm()
    context={'form_contact':form_contact}
    return render(request,'index.html',context)


def DetailViewEco(request):
    
    context={}
    return render(request,'Post_eco.html',context)

def DetailViewJob(request):
    
    context={}
    return render(request,'Post_Job.html',context)