from django.test import SimpleTestCase
from django.urls import reverse
# Create your tests here.
class HomePageTests(SimpleTestCase):
    # test if url exist
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    # test url name for home
    def test_url_name_availabilty(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
    # test if the page is the same that we want
    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h1>Homepage</h1>")
    

        
class AboutPageTests(SimpleTestCase):
    # test if url exist
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)
    # test url name for about
    def test_url_name_availabilty(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
    # test if the page is the same that we want
    def test_template_content(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h1>About page</h1>")