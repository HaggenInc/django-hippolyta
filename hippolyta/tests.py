from django.test import TestCase
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.cache import cache
import hippolyta

TEST_PHRASE = 'Now is the time for all good men to come to the aid of their country.'

class SimpleTest(TestCase):
    def setUp(self):
        if  default_storage.exists('storage_test.txt'):
            default_storage.delete('storage_test.txt')
        file = default_storage.open('storage_read.txt','wb')
        file.write(TEST_PHRASE)
        file.close()


    def test_DoesntExist(self):
        """Test that a file does not exist."""
        self.assertFalse(default_storage.exists('storage_test.txt'))

    def test_OpenSaveFile(self):
        self.assertFalse(default_storage.exists('storage_test.txt'))
        file = default_storage.open('storage_test.txt','wb')
        file.write(TEST_PHRASE)
        file.close()
        self.assertTrue(default_storage.exists('storage_test.txt'))

    def test_OpenReadFile(self):
        file = default_storage.open('storage_read.txt','rb')
        content = file.read()
        file.close()
        self.assertEqual(content, TEST_PHRASE)
    
    def tearDown(self):
        if default_storage.exists('storage_read.txt'):
            default_storage.delete('storage_read.txt')
        if default_storage.exists('storage_test.txt'):
            default_storage.delete('storage_test.txt')
