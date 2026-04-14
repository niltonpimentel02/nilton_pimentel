from django.contrib import messages
from django.conf import settings
# from django.shortcuts import redirect
from django.views.generic import FormView, RedirectView

from .forms import ContactForm


class ContactView(FormView):
    template_name = 'core/contact.html'
    form_class = ContactForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['debug'] = settings.DEBUG
        return context

    def form_valid(self, form):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        messages.error(self.request, 'E-mail não enviado!')
        return self.render_to_response(self.get_context_data(form=form))


class HomeView(RedirectView):
    url = 'contato/'


# def home(request):
#     return redirect('core:contact')
