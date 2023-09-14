from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Review, ReviewComment, Reviewer, Game, Genre
from django.utils import timezone
import datetime

class ReviewerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create_user(username='testuser1', password="Testingcase1")
        test_user1.save()
        temp_reviewer = Reviewer.objects.create(user=test_user1, about='Testing the about')
    
    def test_get_absolute_url(self):
        reviewer = Reviewer.objects.get(user__username='testuser1')
        self.assertEqual(reviewer.get_absolute_url(), '/blog/reviewer/1')
    
    def test_about_max(self):
        reviewer = Reviewer.objects.get(user__username='testuser1')
        max_length = reviewer._meta.get_field('about').max_length
        self.assertEqual(max_length, 500)

class ReviewModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create_user(username='testuser1', password="Testingcase1")
        test_user1.save()
        temp_reviewer = Reviewer.objects.create(user=test_user1, about='Testing the about')
        game = Game.objects.create(name='Test Game', summary='Test Game Summary')
        review = Review.objects.create(title='Test Review 1', reviewer=temp_reviewer, game=game, content='Test Review Content', rating=5)  # Replace 'Test Rating' with an integer rating (e.g., 5)
    
    def test_get_absolute_url(self):
        review = Review.objects.get(title='Test Review 1')
        self.assertEquals(review.get_absolute_url(), '/blog/reviews/1')
    
    def test_content_max(self):
        review = Review.objects.get(id=1)
        max_length = review._meta.get_field('content').max_length
        self.assertEqual(max_length, 5000)
    
    def test_title (self):
        review = Review.objects.get(id=1)
        field_label = review._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')
    
    def test_date(self):
        review = Review.objects.get(id=1)
        datee = review.pub_date
        self.assertEquals(datee, datetime.date.today())

class ReviewCommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(username='testuser', password='testpassword')
        test_review = Review.objects.create(title='Test Review Title', content='Test Review Content')
        test_review_comment = ReviewComment.objects.create(commentor=test_user, comment='Test Comment Content', review=test_review)
    
    def test_content_max(self):
        comment = ReviewComment.objects.get(id=1)
        max_length = comment._meta.get_field('comment').max_length
        self.assertEqual(max_length, 500)
    
    def test_commentor(self):
        comment = ReviewComment.objects.get(id=1)
        commentor = comment.commentor
        self.assertEqual(commentor.username, 'testuser')

    def test_date(self):
        comment = ReviewComment.objects.get(id=1)
        post_date = comment.post_date.date()  
        today = timezone.now().date()
        self.assertEquals(post_date, today)

from django.test import TestCase
from django.urls import reverse
from blog.models import Game, Genre

class GameModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_genre = Genre.objects.create(genre_type='Test Genre')
        game = Game.objects.create(
            name='Test Game',
            summary='Test Game Summary',
        )
        game.genre.add(test_genre)

    def test_name_label(self):
        game = Game.objects.get(id=1)
        field_label = game._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_summary_max_length(self):
        game = Game.objects.get(id=1)
        max_length = game._meta.get_field('summary').max_length
        self.assertEqual(max_length, 1000)

    def test_genre(self):
        game = Game.objects.get(id=1)
        genre = game.genre.first()
        self.assertEqual(genre.genre_type, 'Test Genre')

    def test_get_absolute_url(self):
        game = Game.objects.get(id=1)
        url = reverse('game-detail', args=[str(game.id)])
        self.assertEqual(game.get_absolute_url(), url)
