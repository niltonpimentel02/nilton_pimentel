from django.core import mail
from django.urls import reverse


def test_redirect_home_to_contact_status_code(client):
    response = client.get(reverse('core:home'))
    assert response.status_code == 302


def test_mail(mailoutbox):
    mail.send_mail('subject', 'body', 'from@example.com', ['to@example.com'])
    assert len(mailoutbox) == 1
    m = mailoutbox[0]
    assert m.subject == 'subject'
    assert m.body == 'body'
    assert m.from_email == 'from@example.com'
    assert list(m.to) == ['to@example.com']


def test_contact_form_email_from(client):
    data = dict(
        firstname='Nilton',
        lastname='Pimentel',
        email='email@example.com',
        phone='111111111111111',
        subject='E-mail Enviado Pelo Site Testig',
        message='Testing Testing Testing Testing Testing Testing Testing '
                'Testing Testing Testing Testing Testing Testing Testing'
    )
    client.post(reverse('core:contact'), data)
    email = mail.outbox[0]
    expected = 'contato@niltonpimentel.com.br'
    assert expected == email.from_email


def test_contact_form_status_code_200(client):
    response = client.post(reverse('core:contact'))
    assert response.status_code == 200
