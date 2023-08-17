from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import FormView

from .forms import ContactForm


class ContactView(FormView):
    template_name = 'core/contact.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        form.send_mail()
        messages.success(self.request, 'Email sent successfully!')
        return super().form_valid(form)

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        messages.error(self.request, 'E-mail não enviado!')
        return self.render_to_response(self.get_context_data(form=form))


def home(request):
    return redirect('core:contact')
