from django.test import TestCase
from .models import Something
from django.urls import reverse

class SomethingTest(TestCase):

    def setUp(self):
        Something.objects.create(text= 'testing model in database')

    def test_text_content(self):
        post = Something.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'testing model in database')
                         
class HomePageViewTest(TestCase):

    def setUp(self):
        Something.objects.create(text="this is another test")

    def test_url_expected_location(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)

    def test_url_by_name(self):
        res = self.client.get(reverse('home'))
        self.assertEqual(res.status_code, 200)

    def test_url_on_right_template(self):

        res = self.client.get(reverse('home'))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'home.html')