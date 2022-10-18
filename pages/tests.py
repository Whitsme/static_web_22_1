"""
   Aaron Whitaker
CIS218 - Web Application Programming
9/22/2022 
"""

from django.test import SimpleTestCase
from django.urls import reverse

# The three classes below are used to test the home, contact, and project pages, respectively.
class HomepageTest(SimpleTestCase):
    # Test that the url is at the correct location
    def test_homepage_at_correct_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    # Test that the url is available by name
    def test_homepage_available_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    # Test that the template name is correct
    def test_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    # Test that the template content is correct
    def test_homepage_template_content(self):
        response = self.client.get('/')
        self.assertContains(response, '<h1>Welcome to the Homepage</h1>')

class ContactPageTest(SimpleTestCase):
        # Test that the url is at the correct location
    def test_contact_page_exists_at_correct_location(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

    # Test that the url is available by name
    def test_contact_page_available_by_name(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

    # Test that the template name is correct
    def test_contact_page_template(self):
        response = self.client.get('/contact/')
        self.assertTemplateUsed(response, 'contact.html')

    # Test that the template content is correct
    def test_contact_page_template_content(self):
        response = self.client.get('/contact/')
        self.assertContains(response, '<h1>Contact Me</h1>')

class ProjectsPageTest(SimpleTestCase):
    # Test that the url is at the correct location
    def test_project_page_at_correct_location(self):
        response = self.client.get('/projects/')
        self.assertEqual(response.status_code, 200)

    # Test that the url is available by name
    def test_project_page_available_by_name(self):
        response = self.client.get(reverse('projects'))
        self.assertEqual(response.status_code, 200)

    # Test that the template name is correct
    def test_project_page_template(self):
        response = self.client.get('/projects/')
        self.assertTemplateUsed(response, 'projects.html')

    # Test that the template content is correct
    def test_project_page_template_content(self):
        response = self.client.get('/projects/')
        self.assertContains(response, '<h1>Projects</h1>')
