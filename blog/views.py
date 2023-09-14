from typing import Any
from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from .forms import RegistrationForm
from .models import Game, Genre, Review, ReviewComment, Reviewer, ReviewRequest

def index(request):
    num_games = Game.objects.all().count()
    num_reviews = Review.objects.all().count()
    num_reviewer = Reviewer.objects.count()
    
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    
    context = {
        'num_games': num_games,
        'num_reviews': num_reviews,
        'num_reviewer': num_reviewer,
        'num_visits': num_visits,
    }
    
    return render(request, 'index.html', context=context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index') 
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

class ReviewListView(generic.ListView):
    model = Review
    paginate_by = 10
    
class ReviewDetailView(generic.DetailView):
    model = Review

class ReviewerDetailView(generic.DetailView):
    model = Reviewer
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviewer = self.object
        
        reviews = reviewer.review_set.all()
        context['reviews'] = reviews
        return context

class GameListView(generic.ListView):
    model = Game
    paginate_by = 10

class GameDetailView(generic.DetailView):
    model = Game
    context_object_name = 'game'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        game = self.object
        
        reviews = game.reviews.all()
        context['reviews'] = reviews
        return context

class ReviewCommentCreate(LoginRequiredMixin, CreateView):
    model = ReviewComment
    fields = ['comment',]

    def get_context_data(self, **kwargs):
        context = super(ReviewCommentCreate, self).get_context_data(**kwargs)
        context['review'] = get_object_or_404(Review, pk = self.kwargs['pk'])
        return context
        
    def form_valid(self, form):
        form.instance.commentor = self.request.user
        form.instance.review=get_object_or_404(Review, pk = self.kwargs['pk'])
        return super(ReviewCommentCreate, self).form_valid(form)

    def get_success_url(self): 
        return reverse('review-detail', kwargs={'pk': self.kwargs['pk'],})

def ReviewRequestSuccess(request):
    return render(request, 'blog/review_request_success.html')

class ReviewRequestCreate(LoginRequiredMixin, CreateView):
    model = ReviewRequest
    fields = ['request_game']
    success_url = reverse_lazy('review-request-success')
    