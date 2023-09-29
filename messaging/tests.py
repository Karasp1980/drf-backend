from django.contrib.auth.models import User
from .models import Messaging
from .models import Profile
from rest_framework import status
from rest_framework.test import APITestCase


class ContactListViewTests(APITestCase):
    """
    Tests for the Messaging model list view
    """
    def setUp(self):
        karin = User.objects.create_user(username='karin', password='letmein')
        testson = User.objects.create_user(username='testson', password='pass')
        karins_profile = Profile.objects.get(owner=karin)
        testsons_profile = Profile.objects.get(owner=testson)

    def test_can_list_messaging(self):
        karin = User.objects.get(username='karin')
        testson = User.objects.get(username='testson')
        testsons_profile = Profile.objects.get(id=2)

        Messaging.objects.create(
            owner=karin, profile=testsons_profile, message='hi'
        )
        response = self.client.get('/messaging/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_out_user_cant_create_messaging(self):
        current_user = User.objects.get(username='karin')
        testson = User.objects.get(username='testson')
        profile = Profile.objects.get(id=2)
        response = self.client.post(
            '/messaging/', {
                'owner': current_user, 'profile': profile, 'message': 'hello'
            }
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class MessagingDetailViewTests(APITestCase):
    """
    Tests for the Messaging model detail view
    """
    def setUp(self):
        karin = User.objects.create_user(username='karin', password='letmein')
        testson = User.objects.create_user(username='testson', password='pass')
        testsons_profile = Profile.objects.get(owner=testson)
        karins_profile = Profile.objects.get(owner=karin)
        Messaging.objects.create(
            owner=karin, profile=testsons_profile, message='hello testson'
        )
        Messaging.objects.create(
            owner=testson, profile=karins_profile, message='hello karin'
        )

    def test_cant_retrieve_messaging_using_invalid_id(self):
        response = self.client.get('/messaging/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_can_retrieve_messaging_using_valid_id(self):
        response = self.client.get('/messaging/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
