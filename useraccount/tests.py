from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class RegisterViewTests(TestCase):
    def test_register_view_status_code(self):
        response = self.client.get(reverse("register"))
    #     self.assertEqual(response.status_code, 200)
    # def test_register_view_template_used(self):
    #     response  = self.client.get(reverse('register'))
        #self.assertTemplateUsed(response, '')
    
    def test_register_form_submission(self):
        data = {
            'username': 'testuser',
            'password1': 'password123',
            'password': 'password123',
            'email': 'testuser@gmail.com',
            'langage': 'python'
        }

        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_register_view_redirect_authenticate_user(self):
        self.client.force_login(User.objects.create_user(username= 'existinguser', password='password123'))
        response = self.client.get(reverse('register'))
    