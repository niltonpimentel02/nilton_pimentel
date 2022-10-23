import pytest
from django.test.utils import ignore_warnings
from django.urls import reverse

from ..forms import ContactForm

ignore_warnings(message="No directory at", module="whitenoise.base").enable()

@pytest.fixture
def response(client):
    return client.get(reverse('core:contact'))


def test_form_has_5_fields(response):
    form = ContactForm()
    expected = 5
    assert expected == len(form.fields)


def test_form_has_fields(client):
    response = client.get(reverse('core:contact'))
    expected_name = b'name'
    expected_email = b'email'
    expected_phone = b'phone'
    expected_subject = b'subject'
    expected_message = b'message'
    assert expected_name in response.content
    assert expected_email in response.content
    assert expected_phone in response.content
    assert expected_subject in response.content
    assert expected_message in response.content
