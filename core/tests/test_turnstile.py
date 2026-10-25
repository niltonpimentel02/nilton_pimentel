import json
from unittest.mock import MagicMock

from django.test import override_settings

from helpers.cloudflare import turnstile


@override_settings(CLOUDFLARE_TURNSTILE_SECRET_KEY='test-secret')
def test_verify_turnstile_accepts_success_for_allowed_hostname(monkeypatch):
    response = MagicMock()
    response.__enter__.return_value = response
    response.read.return_value = json.dumps({
        'success': True,
        'hostname': 'www.niltonpimentel.com.br',
    }).encode()
    monkeypatch.setattr(
        turnstile,
        'urlopen',
        lambda request, timeout: response,
    )

    assert turnstile.verify_turnstile('test-token') is True


@override_settings(CLOUDFLARE_TURNSTILE_SECRET_KEY='test-secret')
def test_verify_turnstile_rejects_unapproved_hostname(monkeypatch):
    response = MagicMock()
    response.__enter__.return_value = response
    response.read.return_value = json.dumps({
        'success': True,
        'hostname': 'attacker.example',
    }).encode()
    monkeypatch.setattr(
        turnstile,
        'urlopen',
        lambda request, timeout: response,
    )

    assert turnstile.verify_turnstile('test-token') is False


@override_settings(CLOUDFLARE_TURNSTILE_SECRET_KEY='')
def test_verify_turnstile_rejects_missing_secret(monkeypatch):
    urlopen = MagicMock(side_effect=AssertionError)
    monkeypatch.setattr(turnstile, 'urlopen', urlopen)

    assert turnstile.verify_turnstile('test-token') is False
    urlopen.assert_not_called()
