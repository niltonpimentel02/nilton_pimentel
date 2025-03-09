from decouple import config

CLOUDFLARE_R2_BUCKET = config('CLOUDFLARE_R2_BUCKET')
CLOUDFLARE_R2_ACCESS_KEY = config('CLOUDFLARE_R2_ACCESS_KEY')
CLOUDFLARE_R2_SECRET_KEY = config('CLOUDFLARE_R2_SECRET_KEY')
CLOUDFLARE_R2_BUCKET_ENDPOINT = config('CLOUDFLARE_R2_BUCKET_ENDPOINT')

CLOUDFLARE_R2_CONFIG_OPTIONS = {
    'bucket_name': CLOUDFLARE_R2_BUCKET,
    'access_key': CLOUDFLARE_R2_ACCESS_KEY,
    'secret_key': CLOUDFLARE_R2_SECRET_KEY,
    'endpoint_url': CLOUDFLARE_R2_BUCKET_ENDPOINT,
    'default_acl': 'public-read',
    'signature_version': 's3v4',
}
