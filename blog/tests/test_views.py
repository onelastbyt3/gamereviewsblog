from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Game, Genre, Review, ReviewComment, Reviewer, ReviewRequest
from ..views import ReviewCommentCreate

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.genre = Genre.objects.create(genre_type='Test Genre')
        self.game = Game.objects.create(name='Test Game', summary='Test Game Summary')
        self.game.genre.add(self.genre)
        self.reviewer = Reviewer.objects.create(user=self.user, about='About Test User')
        self.review = Review.objects.create(
            title='Test Review',
            reviewer=self.reviewer,
            game=self.game,
            content='Test Review Content',
            rating=5
        )
        self.comment_data = {
            'comment': 'Test Comment Content'
        }
        self.review_comment_url = reverse('review_comment', kwargs={'pk': self.review.pk})

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_review_list_view(self):
        response = self.client.get(reverse('reviews'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/review_list.html')

    def test_review_detail_view(self):
        response = self.client.get(reverse('review-detail', kwargs={'pk': self.review.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/review_detail.html')

    def test_reviewer_detail_view(self):
        response = self.client.get(reverse('reviewer-detail', kwargs={'pk': self.reviewer.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/reviewer_detail.html')

    def test_game_list_view(self):
        response = self.client.get(reverse('games'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/game_list.html')

    def test_game_detail_view(self):
        response = self.client.get(reverse('game-detail', kwargs={'pk': self.game.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/game_detail.html')

    def test_review_comment_create_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.review_comment_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/reviewcomment_form.html')
        
    def test_review_comment_create_form_valid(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(self.review_comment_url, data=self.comment_data)
        self.assertEqual(response.status_code, 302)  

    def test_review_request_create_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('review-request'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/reviewrequest_form.html')

    def test_review_request_create_form_valid(self):
        self.client.login(username='testuser', password='testpassword')
        request_data = {'request_game': self.game.id}
        response = self.client.post(reverse('review-request'), data=request_data)
        self.assertEqual(response.status_code, 302)  
        self.assertRedirects(response, reverse('review-request-success'))
