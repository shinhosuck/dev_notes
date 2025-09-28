from django.test import TestCase, RequestFactory
from accounts.models import Profile
from django.contrib.auth import get_user_model
from django.utils.text import slugify

User = get_user_model()

class TestProfileModel(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username='jack', password='12345')
        Profile.objects.create(first_name='Greg', last_name='Smith')

        cls.uri = 'http://testserver/avatars/default.png'
        cls.user = User.objects.get(username='jack')
        cls.profile = Profile.objects.get(slug='greg')
        cls.factory = RequestFactory()

    def test_str_method(self):
        self.assertEqual(str(self.profile), 'Greg')

    def test_likes(self):
        self.profile.likes.add(self.user)
        self.assertEqual(self.profile.likes.count(), 1)

    def test_slug(self):
        url = self.profile.get_absolute_url()
        self.assertEqual(url, '/profile/greg/')

    def test_build_absolute_uri(self):
        request = self.factory.get(self.profile.get_absolute_url())
        uri = self.profile.get_absolute_avatar_uri(request)
        self.assertEqual(uri, self.uri)

