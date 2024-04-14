from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from blog_app.models import Post, Comment
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import AccessToken

class APITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='test_user', password='password')
        self.access_token = str(AccessToken.for_user(self.user))
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_post_creation(self):
        url = reverse('post-list-create')
        data = {'title': 'New Post', 'content': 'New Content'}
        resp = self.client.post(url, data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

    def test_post_list(self):
        url = reverse('post-list-create')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_post_detail(self):
        post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)
        url = reverse('post-detail', kwargs={'pk': post.pk})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_post_update(self):
        post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)
        url = reverse('post-detail', kwargs={'pk': post.pk})
        data = {'title': 'Updated Post', 'content': 'Updated Content'}
        resp = self.client.put(url, data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_post_deletion(self):
        post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)
        url = reverse('post-detail', kwargs={'pk': post.pk})
        resp = self.client.delete(url)
        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)

    def test_comment_creation(self):
        post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)
        comment_creation_url = reverse('post-comment-list', kwargs={'post_id': post.pk})
        comment_data = {'text': 'New Comment', 'author': self.user.id, 'post': post.pk} 
        comment_resp = self.client.post(comment_creation_url, comment_data, format='json')
        self.assertEqual(comment_resp.status_code, status.HTTP_201_CREATED)

    def test_comment_list(self):
        post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)
        url = reverse('post-comment-list', kwargs={'post_id': post.pk})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_comment_detail(self):
        post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)
        comment = Comment.objects.create(post=post, text='Test Comment', author=self.user)  
        url = reverse('post-comment-detail', kwargs={'post_id': post.pk, 'pk': comment.pk})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_comment_update(self):
        post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)
        comment = Comment.objects.create(post=post, text='Test Comment', author=self.user)
        url = reverse('post-comment-detail', kwargs={'post_id': post.pk, 'pk': comment.pk}) 
        comment_data = {'text': 'updated Comment', 'author': self.user.id, 'post': post.pk} 
        resp = self.client.put(url, comment_data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_comment_deletion(self):
        post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)
        comment = Comment.objects.create(post=post, text='Test Comment', author=self.user)  # Changed 'content' to 'text'
        url = reverse('post-comment-detail', kwargs={'post_id': post.pk, 'pk': comment.pk})  # Updated URL with post_id
        resp = self.client.delete(url)
        print(resp.data)
        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)

    def test_like_post(self):
        post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)
        url = reverse('like-post', kwargs={'pk': post.pk, 'type': 'post'})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        post.refresh_from_db()
        self.assertEqual(post.likes, 1)
        self.assertIn(self.user, post.liked_by.all())

    def test_unlike_post(self):
        post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)
        post.liked_by.add(self.user)
        post.likes += 1
        post.save()
        
        url = reverse('like-post', kwargs={'pk': post.pk, 'type': 'post'})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        post.refresh_from_db()
        self.assertEqual(post.likes, 0)
        self.assertNotIn(self.user, post.liked_by.all())

    def test_like_comment(self):
        post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)
        comment = Comment.objects.create(post=post, text='Test Comment', author=self.user)
        
        url = reverse('like-comment', kwargs={'pk': comment.pk, 'type': 'comment'})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        comment.refresh_from_db()
        self.assertEqual(comment.likes, 1)
        self.assertIn(self.user, comment.liked_by.all())

    def test_unlike_comment(self):
        post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)
        comment = Comment.objects.create(post=post, text='Test Comment', author=self.user)
        
        comment.liked_by.add(self.user)
        comment.likes += 1
        comment.save()
        
        url = reverse('like-comment', kwargs={'pk': comment.pk, 'type': 'comment'})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        comment.refresh_from_db()
        self.assertEqual(comment.likes, 0)
        self.assertNotIn(self.user, comment.liked_by.all())
