from django.contrib.auth.models import User
from .models import Adoption
from rest_framework import status
from rest_framework.test import APITestCase


class AdoptionpostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='karin', password='pass')

    def test_can_list_adoptionposts(self):
        karin = User.objects.get(username='karin')
        Adoption.objects.create(owner=karin, title='a title')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_adoptionpost(self):
        self.client.login(username='karin', password='pass')
        response = self.client.post('/adoption/', {'title': 'a title'})
        count = Adoption.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_adoptionpost(self):
        response = self.client.post('/adoption/', {'title': 'a title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class AdoptionpostDetailViewTests(APITestCase):
    def setUp(self):
        karin = User.objects.create_user(username='karin', password='pass')
        kim = User.objects.create_user(username='kim', password='pass')
        Adoption.objects.create(
            owner= karin, title='a title', content='karins content'
        )
        Adoption.objects.create(
            owner=kim, title='another title', content='kims content'
        )
    
    def test_can_retrieve_adoptionpost_using_valid_id(self):
        response = self.client.get('/adoption/1/')
        self.assertEqual(response.data['title'], 'a title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_adoptionpost_using_invalid_id(self):
        response = self.client.get('/adoption/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_adoptionpost(self):
        self.client.login(username='karin', password='pass')
        response = self.client.put('/adoption/1/', {'title': 'a new title'})
        adoption = Adoption.objects.filter(pk=1).first()
        self.assertEqual(adoption.title, 'a new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_user_cant_update_another_users_adoptionpost(self):
        self.client.login(username='karin', password='pass')
        response = self.client.put('/adoption/2/', {'title': 'a new title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
