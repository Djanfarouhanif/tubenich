from django.test import TestCase, Client
from django.urls import reverse


class  TestLoaderVideo(TestCase):
    def setUp(self):
        self.urls_lader = reverse('loader')
        self.client = Client()

    def testSucces(self):
        data = {
            'search': 'search',
            'langage': 'langage',
            'number': '1'
        }
        response = self.client.post(self.urls_lader, data)

        self.assertEqual(response.status_code, 200)