from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from lists.views import homePage

# Create your tests here.
class HomePageTest(TestCase):
  def test_root_url_resolves_to_home_page_view(self):
    found = resolve("/")
    self.assertEqual(found.func, homePage)
  def test_home_page_returns_correct_html(self):
    request = HttpRequest()
    response = homePage(request)
    expected_html = render_to_string('index.html')
    self.assertEqual(response.content.decode(), expected_html)