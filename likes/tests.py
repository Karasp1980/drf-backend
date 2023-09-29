from django.test import TestCase
from django.contrib.auth.models import User
from posts.models import Post
from .models import Like


class LikeTestCase(TestCase):
    """Test for Like Model"""

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass')
        self.post = Post.objects.create(title='Test Post', owner=self.user)
        self.like = Like.objects.create(owner=self.user, post=self.post)

    def test_like_instance(self):
        """Test for Like instance"""
        self.assertTrue(isinstance(self.like, Like))
        self.assertEqual(self.like.__str__(), f'{self.like.owner} {self.like.post}')

    def test_unique_together(self):
        """Test for unique_together in Meta class"""
        with self.assertRaises(Exception) as raised:
            Like.objects.create(owner=self.user, post=self.post)
        self.assertEqual(raised.exception.args[0], 'UNIQUE constraint failed: likes_like.owner_id, likes_like.post_id')

   


