from django.test import TestCase
from django.urls import reverse


class RootTestCase(TestCase):
    def test_index(self):
        response = self.client.get(reverse("root:index"))
        self.assertTemplateUsed(response, "root/index.html")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This is Django demo app main page")
        self.assertEqual(response.context["active_page"], "index")

    def test_about(self):
        response = self.client.get(reverse("root:about"))
        self.assertTemplateUsed(response, "root/about.html")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "About this Django demo app")
        self.assertEqual(response.context["active_page"], "about")
