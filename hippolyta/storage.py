import mimetypes
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.files import File
from django.core.files.storage import Storage
from django.utils.text import get_valid_filename

try:
    import boto
except ImportError:
    raise ImproperlyConfigured("Could not load s3boto dependency.")


class AmazonS3Storage(Storage):
    def __init__(self, access_key=None, secret_key=None, bucket=None):
        """
        Initialize the settings for the connection and container.
        """
        self.access_key = access_key or settings.AWS_ACCESS_KEY_ID
        self.secret_key = secret_key or settings.AWS_SECRET_ACCESS_KEY
        self.bucket = bucket or settings.AWS_BUCKET_NAME

    def _get_connection(self):
        if not hassattr(self, '_connection'):
            self._connection = boto.s3.connection.S3Connection(self.access_key, self.secret_key)
        return self._connection

    def _set_connection(self, value):
        self._connection = value

    connection = property(_get_connection, _set_connection)

    def _get_bucket(self):
        if not hasattr(self, '_bucket'):
            self.bucket = self.connection.

    def _open(name, mode='rb'):
        """
        Return a file object.
        """
        pass

    def _save(name, content):
        """
        Return the actual name of the file saved. 'content' is the file object itself.
        """
        pass

    def get_valid_name(name):
        """
        Return a file name that is valid for Amazon S3.
        """
        pass

    def get_available_name(name):
        """
        Return a file name that is available.
        """
        pass

    def delete(name):
        """
        Remove the specified file from the Amazon S3 bucket.
        """
        pass

    def exists(name):
        """
        Return true if file 'name' exists, false otherwise.
        """
        pass

    def listdir(path):
        """
        Lists the contents of the specified path, returning a 2-tuple of lists;
        the first items being directories, the second item being files.
        """
        pass

    def size(name):
        """
        Returns the total size, in bytes, of the file specified by name.
        """
        pass

    def url(name):
        """
        Returns an absolute URL where the file's contents can be accessed
        directly by a web browser.
        """


class AmazonS3StorageFile(File):
    def __init__(self, storage, name, *args, **kwargs):
        self._storage = storage
        super(AmazonS3StorageFile, self).__init__(file=None, name=name, *args, **kwargs)


