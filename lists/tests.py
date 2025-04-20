from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
class HomePageTest(TestCase):
    
    def test_home_page_returns_correct_html(self):
        reponse = self.client.get('/')
        self.assertTemplateUsed(reponse, 'home.html')