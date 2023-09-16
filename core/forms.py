from django import forms
from django.conf import settings
from django.core.mail import get_connection
from django.core.mail.message import EmailMessage
from django.http import JsonResponse


class ContactForm(forms.Form):
    name = forms.CharField(
        label='',
        max_length=100,
        error_messages={'required': 'Por favor, digite seu nome:'},
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
    )
    email = forms.EmailField(
        label='',
        max_length=100,
        error_messages={'required': 'Por favor, digite seu email:'},
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
    )
    phone = forms.CharField(
        label='',
        max_length=20,
        error_messages={'required': 'Por favor, digite seu celular:'},
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Celular',
                'id': 'id_phone',
            }
        )
    )
    subject = forms.CharField(
        label='',
        max_length=100,
        error_messages={'required': 'Por favor, digite um assunto:'},
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Assunto'}),
    )
    message = forms.CharField(
        label='',
        error_messages={'required': 'Por favor, digite sua mensagem:'},
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mensagem'}),
    )

    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        phone = self.cleaned_data['phone']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']

        body = f'Nome: {name}\nE-mail: {email}\nCelular: {phone}\nAssunto: {subject}\nMensagem: {message}'

        with get_connection(
            host=settings.EMAIL_HOST,
            port=settings.EMAIL_PORT,
            username=settings.EMAIL_USER,
            password=settings.EMAIL_PASSWORD,
            use_tls=True,
        ) as connection:
            mail = EmailMessage(
                subject='E-mail enviado pelo site',
                body=body,
                to=['contato@niltonpimentel.com.br', ],
                from_email=settings.DEFAULT_FROM_EMAIL,
                connection=connection,
            )
            mail.send()

        return JsonResponse({"status": "ok"})
