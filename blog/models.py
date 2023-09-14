from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

class Reviewer(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    about = models.TextField(max_length=500, help_text="Write a short blurb about yourself.")
    
    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse("reviewer-detail", args=[str(self.id)])

class Review(models.Model): 
    title = models.CharField(max_length=200)
    reviewer = models.ForeignKey(Reviewer, on_delete=models.SET_NULL, null=True)
    game = models.ForeignKey('Game', on_delete=models.SET_NULL, null=True)
    content = models.TextField(max_length=5000, help_text="Enter your review here.")
    pub_date = models.DateField(default=date.today)
    rating = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])

    class Meta:
        ordering = ['-pub_date']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("review-detail", args=[str(self.id)])

class Genre(models.Model):
    genre_type = models.CharField(max_length=50, help_text="Enter a game genre (i.e. Action, Puzzle)")
    
    def __str__(self):
        return self.genre_type

class Game(models.Model):
    name = models.CharField(max_length=100)
    summary = models.TextField(max_length=1000, help_text="Enter a short summary of this game.")
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this game.")
    reviews = models.ManyToManyField(Review, blank=True, related_name='games')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("game-detail", args=[str(self.id)])

class ReviewComment(models.Model):
    comment = models.TextField(max_length=500, help_text="Write your comments here.")
    commentor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)

    class Meta:
        ordering = ['post_date']
    
    def __str__(self):
        return self.comment

class ReviewRequest(models.Model):
    request_game = models.TextField(max_length=100)
    
    def __str__(self):
        return self.request_game

    def get_absolute_url(self):
        return reverse("review-request", args=[str(self.id)])