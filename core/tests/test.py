from django.test import TestCase
from django.contrib.auth.models import User


class ApisTestCase(TestCase):
    def setUp(self):
        """
        A funcao esta criando um modelo de User
        @param1: username
        @param2: email
        @param3: client_ip_address
        """
        User.objects.create(
            username='samuel',
            email='samuelfernandes2196@gmail.com',
            password='010203sa'
        )


    def test_create_new_api_logs_model(self):
        """
        A funcao esta certificando de que esta sendo 
        criado o modelo User
        @param1: username
        """
        username = User.objects.get(username='samuel')
        self.assertEqual(username.__str__(), 'samuel')

