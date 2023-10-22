from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class AuthenticationTestCase(TestCase):
    
    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.user_data = {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'testuser@example.com',
            "first_name": "testname",
            "last_name": "testsurname"
        }
        self.user = User.objects.create_user(**self.user_data)
        
    def tearDown():
        pass
        
    
    def test_register_new_user(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(self.register_url, self.user_data)
        self.assertEqual(response.status_code, 302)  

        # Check if the user is created
        self.assertTrue(User.objects.filter(username='testuser').exists())
    def register_existing_user():
        pass
    def login_correct_credentaials():
        pass
    def login_incorrect_credentials():
        pass