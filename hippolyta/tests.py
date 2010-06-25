from django.test import TestCase
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.cache import cache
import hippolyta

class SimpleTest(TestCase):
    def setUp(self):
        if default_storage.exists('storage_test'):
            default_storage.delete('storage_test')

    def test_DoesntExist(self):
        """Test that a file does not exist."""
        self.assertFalse(default_storage.exists('storage_test'))

    def test_OpenReadFile(self):
        file = default_storage.open('notes.txt','rb')
        content = file.read()
        file.close()

    def test_OpenSaveFile(self):
        self.assertFalse(default_storage.exists('storage_test.txt'))
        file = default_storage.open('storage_test.txt','wb')
        file.write('Now is the time for all good men to come to the aid of their country.')
        file.close()
    
    def tearDown(self):
        if default_storage.exists('storage_test.txt'):
            default_storage.delete('storage.test.txt')
