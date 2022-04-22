from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError




def index(request):
    
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message'] + " \n" + from_email
            try:
                send_mail(subject, message, 'bot.django.portefolio@gmail.com', ['ayoubhaddou1@gmail.com'],fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            # render( request, 'index.html', {'email_send': True, 'subject' : subject})
            return redirect('success')
    return render( request, 'index.html', {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')