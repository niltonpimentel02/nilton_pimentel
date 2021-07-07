from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import ContactForm


def contact(request):
    form = ContactForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail()
            messages.success(request, 'E-mail enviado com sucesso!')
            form = ContactForm()
        else:
            messages.error(request, 'E-mail não enviado!')
    context = {
        'form': form
    }
    return render(request, 'core/contact.html', context)

def home(request):
    return redirect('core:contact')
