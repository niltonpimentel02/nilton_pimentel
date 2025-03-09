from storages.backends.s3 import S3Storage


class MediaFileStorage(S3Storage):
    """
    For general uploads
    """

    location = 'media'


class StaticFileStorage(S3Storage):
    """
    For staticfiles
    """

    location = 'static'
