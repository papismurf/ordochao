<<<<<<< HEAD
from django.template.loader import render_to_string
from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

# from lists.views import home_page

# Create your tests here.


class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
#       request = HttpRequest()
#       response = home_page(request)
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')
=======
from django.template.loader import render_to_string
from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

# from lists.views import home_page

# Create your tests here.


class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
#       request = HttpRequest()
#       response = home_page(request)
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')
>>>>>>> 978be58aa72e1dfc76afeb677f114895df88544e
