from django.test import TestCase

# Create your tests here.
class SmokeTests(TestCase):
    def test_basicmath(self):
        self.assertEqual(1+1, 11) #goblok
        