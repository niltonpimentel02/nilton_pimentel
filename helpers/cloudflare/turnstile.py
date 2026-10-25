import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from django.conf import settings


SITEVERIFY_URL = 'https://challenges.cloudflare.com/turnstile/v0/siteverify'
ALLOWED_HOSTNAMES = {
    'niltonpimentel.com.br',
    'www.niltonpimentel.com.br',
}


def verify_turnstile(token):
    secret = settings.CLOUDFLARE_TURNSTILE_SECRET_KEY
    if not token or not secret:
        return False

    request = Request(
        SITEVERIFY_URL,
        data=urlencode({'secret': secret, 'response': token}).encode(),
        headers={'Content-Type': 'application/x-www-form-urlencoded'},
    )

    try:
        with urlopen(request, timeout=10) as response:
            result = json.loads(response.read())
    except (OSError, ValueError):
        return False

    return (
        isinstance(result, dict)
        and result.get('success') is True
        and result.get('hostname') in ALLOWED_HOSTNAMES
    )
