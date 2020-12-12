from django.test import TestCase, Client



from django.urls import reverse


class WorkoutViewTest(TestCase):
    def setUp(self):
        self.test_client = Client()

    def test_render_corect_template_with_not_core_workout(self):
        response = self.test_client.get(reverse('register_user'))
        self.assertTemplateUsed(response, 'testing/home_page.html')