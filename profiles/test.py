from django.contrib.auth.models import User
from .models import Profile
from rest_framework import status
from rest_framework.test import APITestCase


class ProfileListViewTests(APITestCase):
    """
    Tests for the Profile model list view
    """
    def setUp(self):
        karin = User.objects.create_user(username='karin', password='letmein')
        testson = User.objects.create_user(username='testson', password='pass')
        
    def test_profile_automatically_created_on_user_creation(self):
        response = self.client.get('/profiles/')
        count = Profile.objects.count()
        self.assertEqual(count, 2)

    def test_can_list_profiles(self):
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ProfileDetailViewTests(APITestCase):
    """
    Tests for the Profile model detail view
    """
    def setUp(self):
        karin = User.objects.create_user(username='karin', password='letmein')
        testson = User.objects.create_user(username='testson', password='pass')

    def test_cant_retrieve_profile_using_invalid_id(self):
        response = self.client.get('/profiles/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_can_retrieve_profile_using_valid_id(self):
        response = self.client.get('/profiles/2/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_update_own_profile(self):
        self.client.login(username='karin', password='letmein')
        response = self.client.put(
            '/profiles/1/', {'name': 'Karin'}
        )
        profile = Profile.objects.filter(pk=1).first()
        self.assertEqual(profile.name, 'Karin')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_someone_elses_profile(self):
        self.client.login(username='karin', password='letmein')
        response = self.client.put(
            '/profiles/2/', {'bio': 'I want to edit Testsons bio'}
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


   

   

   