from django.test import TestCase
from django.contrib.auth.models import User


class TestRawEnter(TestCase):
    def test_entry(self):
        response = self.client.get('')
        # import pdb; pdb.set_trace()
        self.assertIn(b'<h2>Welcome to the home page!</h2>', response.content)

    def test_entry_code(self):
        response = self.client.get('')
        # import pdb; pdb.set_trace()
        self.assertEqual(200, response.status_code)

    def test_entry_nofound(self):
        response = self.client.get('chat')
        # import pdb; pdb.set_trace()
        self.assertIn(b'<h1>Not Found</h1><p>The requested resource was not found on this server.</p>', response.content)

    def test_entry_nofound_code(self):
        response = self.client.get('chat')
        # import pdb; pdb.set_trace()
        self.assertEqual(404, response.status_code)

    def test_entry_chat(self):
        response = self.client.get('/chat/')
        # import pdb; pdb.set_trace()
        self.assertIn(b'<title>Chat Rooms</title>', response.content)

    def test_entry_chat_code(self):
        response = self.client.get('/chat/')
        # import pdb; pdb.set_trace()
        self.assertEqual(200, response.status_code)

    def test_entry_resort(self):
        response = self.client.get('/api/v1/resort/')
        self.assertEqual(200, response.status_code)


class TestLoginEnter(TestCase):
    """
    """
    def setUp(self):
        self.test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        self.test_user2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD')
        self.test_user1.save()
        self.test_user2.save()

    def test_login_entry(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get('')
        # import pdb; pdb.set_trace()
        self.assertIn(b'<h3>You\'re currently logged in as testuser1</h3>\n', response.content)

    def test_login_entry_code(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get('')
        # import pdb; pdb.set_trace()
        self.assertEqual(200, response.status_code)
