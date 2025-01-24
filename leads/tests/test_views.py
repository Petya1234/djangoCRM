from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class LandingPageTest(TestCase):
    
    def test_get_request(self):
        response = self.client.get(reverse("landing_page"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateNotUsed(response, "landing.html")
    
       