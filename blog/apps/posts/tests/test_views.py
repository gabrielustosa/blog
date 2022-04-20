from django.urls import reverse

from blog.apps.posts.tests.test_base import PostTestBase


class PostViewsTest(PostTestBase):
    def setUp(self):
        self.make_post()
        self.url = reverse('post:detail_view', kwargs={'id': 1})
        self.response = self.client.get(self.url)

    def test_post_detail_page_return_status_code_200(self):
        self.assertEqual(self.response.status_code, 200)

    def test_post_detail_page_loads_correct_template(self):
        self.assertTemplateUsed(self.response, 'post/detail_view.html')
