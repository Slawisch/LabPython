from django.test import TestCase
from django.urls import reverse


class HomeTests(TestCase):
    def test_index_view_status_code(self):
        url = reverse('media:index')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_detail_view_status_code(self):
        link_id = 1
        url = reverse('media:detail', args=(link_id,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_addLikeDislike_view_status_code(self):
        link_id = 1
        url = reverse('media:addLikeDislike', args=(link_id,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)