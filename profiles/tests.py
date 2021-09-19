from config import settings
from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.
User = get_user_model()

class UserTestCase(TestCase):
    def setUp(self):
        test_user = User(username='test_user', email='testuser@gm.com')
        test_user.is_staff = True
        test_user.is_superuser = True
        self.test_user_pass = 'Haslo901'
        test_user.set_password(self.test_user_pass)
        test_user.save()
        self.test_user = test_user

    def test_user_exists(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)
        self.assertNotEqual(user_count, 0)

    def test_user_password(self):
        self.assertTrue(self.test_user.check_password(self.test_user_pass))

    def test_login_url(self):
        login_url = settings.LOGIN_URL
        data = {'username':'test_user', 'password':self.test_user_pass}
        response = self.client.post(login_url, data, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        #log and check logout
        self.client.login(username='test_user', password=self.test_user_pass)
        response = self.client.get('')
        self.assertEquals(response.status_code, 200)
        self.client.logout()
        response = self.client.get('/profiles/login/')
        self.assertEquals(response.status_code, 200)
