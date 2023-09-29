from django.contrib.auth.models import User
from .models import Follower
from rest_framework import status
from rest_framework.test import APITestCase


class FollowerListViewTests(APITestCase):
    """
    Tests for the Follower model list view
    """
    def setUp(self):
        karin = User.objects.create_user(username='karin', password='letmein')
        testson = User.objects.create_user(username='testson', password='pass')
        kim = User.objects.create_user(username='kim', password='secret')
        Follower.objects.create(owner=karin, followed=testson)

    def test_can_view_follower_list(self):
        karin = User.objects.get(username='karin')
        response = self.client.get('/followers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_out_user_cant_follow(self):
        karin = User.objects.get(username='karin')
        kim = User.objects.get(username='kim')
        response = self.client.post(
            '/followers/', {'owner': karin, 'followed': kim}
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        count = Follower.objects.count()
        self.assertEqual(count, 1)

    def test_logged_in_user_can_follow(self):
        """
        In this test, karin will login and follow kim
        """
        self.client.login(username='karin', password='letmein')
        response = self.client.post(
            '/followers/', {'owner': 1, 'followed': 3}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_in_user_cant_follow_someone_they_already_follow(self):
        """
        In this test, karin will login and try to follow testson again
        """
        self.client.login(username='karin', password='letmein')
        response = self.client.post(
            '/followers/', {'owner': 1, 'followed': 2}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class FollowerDetailViewTests(APITestCase):
    """
    Tests for the Follower model detail view
    """
    def setUp(self):
        karin = User.objects.create_user(username='karin', password='letmein')
        testson = User.objects.create_user(username='testson', password='pass')
        kim = User.objects.create_user(username='kim', password='secret')
        Follower.objects.create(owner=karin, followed=kim)

    def test_cant_retrieve_follow_using_invalid_id(self):
        response = self.client.get('/followers/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_can_retrieve_follow_using_valid_id(self):
        response = self.client.get('/followers/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_unfollow_a_user(self):
        self.client.login(username='karin', password='letmein')
        response = self.client.delete('/followers/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_cant_unfollow_if_not_logged_in(self):
        response = self.client.delete('/followers/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
