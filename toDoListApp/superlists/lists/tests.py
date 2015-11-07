from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from lists.views import homePage
from django.template.loader import render_to_string

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
  def test_home_page_can_save_a_POST_request(self):
    request = HttpRequest()
    request.method = 'POST'
    request.POST['item_text'] = 'A new list item'
    
    response = homePage(request)
    
    self.assertIn('A new list item', response.content.decode())
    expected_html = render_to_string(
      'index.html',
      {'new_item_text': 'A new list item'},
    )
    self.assertEqual(response.content.decode(), expected_html)