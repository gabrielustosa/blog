from django.urls import reverse

from blog.apps.posts.tests.test_base import PostTestBase


class PageViewTest(PostTestBase):
    def setUp(self):
        self.url = reverse('page:home')
        self.response = self.client.get(self.url)

    def test_home_page_return_status_code_200(self):
        self.assertEqual(self.response.status_code, 200)

    def test_home_page_loads_correct_template(self):
        self.assertTemplateUsed(self.response, 'pages/home.html')

    def test_home_page_dont_show_not_published_posts(self):
        self.make_post(is_published=False)
        response = self.client.get(self.url)
        self.assertEqual(len(response.context['posts']), 0)

