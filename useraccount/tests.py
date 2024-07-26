from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Student


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
            'last_name': 'test',
            'password1': 'password123',
            'password': 'password123',
            'email': 'testuser@gmail.com',
            'langage': 'python'
        }

        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='testuser').exists())
        user = User.objects.get(username='testuser')
        self.assertTrue(Student.objects.filter(user=user).exists())

    def test_register_view_redirect_authenticate_user(self):
        self.client.force_login(User.objects.create_user(username= 'existinguser', password='password123'))
        response = self.client.get(reverse('register'))
class LoginViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username = 'hanif', password='1234')
        self.login_urls = reverse('login')

    def testLogin_succes(self):
        data = {
            'username': 'hanif',
            'password': '1234'
        }
        response = self.client.post(self.login_urls, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))