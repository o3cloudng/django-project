from rest_framework.test import APITestCase
from authentication.models import User

class TestModel(APITestCase):

    def test_creates_user(self):
        # self.assertEqual(1,1-0)
        user=User.objects.create_user('Olumide', 'o3cloudng@gmail.com', '$Password!')
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, 'o3cloudng@gmail.com')

    def test_raises_error_when_no_username_is_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user, username="", email='o3cloudng@gmail.com', password='$Password!')
    
    def test_raises_error_with_message_when_no_username_is_supplied(self):
        with self.assertRaisesMessage(ValueError, 'The given username must be set'):
            User.objects.create_user(username='', email='o3cloudng@gmail.com', password='$Password!')


    def test_raises_error_when_no_email_is_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user, username="Olumide", email='', password='$Password!')

    def test_raises_error_with_message_when_no_email_is_supplied(self):
        with self.assertRaisesMessage(ValueError, 'The given email must be set'):
            User.objects.create_user(username='Olumide', email='', password='$Password!')

    def test_creates_super_user(self):
        # self.assertEqual(1,1-0)
        user=User.objects.create_superuser('Olumide', 'o3cloudng@gmail.com', '$Password!')
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email, 'o3cloudng@gmail.com')

    
    def test_creates_super_user_with_is_staff_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_staff=True.'):
            User.objects.create_superuser(username='Olumide', email='o3cloudng@gmail.com', password='$Password!', is_staff=False)

    def test_creates_super_user_with_super_user_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_superuser=True.'):
            User.objects.create_superuser(username='Olumide', email='o3cloudng@gmail.com', password='$Password!', is_superuser=False)

