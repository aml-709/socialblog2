from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token

from usersup.models import Post

User = get_user_model()

class AuthTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
        )
        self.url = reverse('post_list')

    def test_session_authentication(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.logout()


    def test_token_authentication(self):
        token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class PostAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
        )
        self.client.login(username='testuser', password='testpassword')
        

class PostAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
        )
        self.client.login(username='testuser', password='testpassword')  
        self.url = reverse('create_test_post')  

    def test_create_post(self):
        data = {'content': 'Test post content'}
        response = self.client.post(self.url, data, format='json')  
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  
        self.assertEqual(Post.objects.count(), 1) 
        self.assertEqual(Post.objects.first().content, 'Test post content') 

    def test_get_post_list(self):
        url = reverse('post_list') 
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)






