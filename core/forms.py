from django import forms
from django.conf import settings
from django.core.mail import get_connection
from django.core.mail.message import EmailMessage
from django.http import JsonResponse


class ContactForm(forms.Form):
    firstname = forms.CharField(
        label='',
        min_length=3,
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Nome'}),
    )
    lastname = forms.CharField(
        label='',
        min_length=3,
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Sobrenome'}),
    )
    email = forms.EmailField(
        label='',
        min_length=8,
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Email'}),
    )
    phone = forms.CharField(
        label='',
        min_length=15,
        widget=forms.TextInput(attrs={'placeholder': 'Celular', 'data-mask': '(00) 00000-0000'}),
    )
    subject = forms.CharField(
        label='',
        min_length=25,
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Assunto'}),
    )
    message = forms.CharField(
        label='',
        min_length=100,
        max_length=1000,
        widget=forms.Textarea(attrs={'placeholder': 'Mensagem'}),
    )

    def send_mail(self):
        firstname = self.cleaned_data['firstname'].title()
        lastname = self.cleaned_data['lastname'].title()
        email = self.cleaned_data['email'].lower()
        phone = self.cleaned_data['phone']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']

        body = (
            f'Nome: {firstname}\n'
            f'Sobrenome: {lastname}\n'
            f'E-mail: {email}\n'
            f'Celular: {phone}\n'
            f'Assunto: {subject}\n'
            f'Mensagem: {message}\n'
        )

        with get_connection(
            host=settings.EMAIL_HOST,
            port=settings.EMAIL_PORT,
            username=settings.EMAIL_USER,
            password=settings.EMAIL_PASSWORD,
            use_tls=True,
        ) as connection:
            mail = EmailMessage(
                subject='E-mail Enviado Pelo Site',
                body=body,
                to=['contato@niltonpimentel.com.br', ],
                from_email=settings.DEFAULT_FROM_EMAIL,
                connection=connection,
            )
            mail.send()

        return JsonResponse({'status': 'ok'})
