import pytest
from django.urls import reverse

from ..forms import ContactForm


@pytest.fixture
def response(client):
    return client.get(reverse('core:contact'))


def test_form_has_6_fields(response):
    form = ContactForm()
    expected = 6
    assert expected == len(form.fields)


def test_form_has_fields(client):
    response = client.get(reverse('core:contact'))
    expected_firstname = b'firstname'
    expected_lastname = b'lastname'
    expected_email = b'email'
    expected_phone = b'phone'
    expected_subject = b'subject'
    expected_message = b'message'
    assert expected_firstname in response.content
    assert expected_lastname in response.content
    assert expected_email in response.content
    assert expected_phone in response.content
    assert expected_subject in response.content
    assert expected_message in response.content
