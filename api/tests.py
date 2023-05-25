from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import User, Post
from .serializers import UserSerializer, PostSerializer

class UserTests(TestCase):
    def test_create_user(self):
        """
        Test creating a new user
        """
        # Crie um usuário de exemplo
        user_data = {
            'username': 'johndoe',
            'email': 'johndoe@example.com',
            'password': 'password123'
        }
        response = self.client.post(reverse('user-registration'), user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'johndoe')

class PostTests(APITestCase):
    def setUp(self):
        # Crie um usuário de exemplo
        self.user = User.objects.create_user(username='johndoe', password='password123')
        # Crie uma postagem de exemplo
        self.post_data = {
            'title': 'Test Post',
            'content': 'This is a test post',
            'author': self.user.id
        }

    def test_create_post(self):
        """
        Test creating a new post
        """
        response = self.client.post(reverse('post-create'), self.post_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().title, 'Test Post')
        self.assertEqual(Post.objects.get().author, self.user)

    def test_list_posts(self):
        """
        Test listing all posts
        """
        # Crie algumas postagens de exemplo
        Post.objects.create(title='Post 1', content='Content 1', author=self.user)
        Post.objects.create(title='Post 2', content='Content 2', author=self.user)

        response = self.client.get(reverse('post-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

class ModelTests(TestCase):
    def test_user_model(self):
        """
        Test User model
        """
        user = User.objects.create_user(username='johndoe', password='password123')
        self.assertEqual(user.username, 'johndoe')
        # Add more assertions as needed

    def test_post_model(self):
        """
        Test Post model
        """
        user = User.objects.create_user(username='johndoe', password='password123')
        post = Post.objects.create(title='Test Post', content='This is a test post', author=user)
        self.assertEqual(post.title, 'Test Post')
        # Add more assertions as needed
